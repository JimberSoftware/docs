#!/usr/bin/env python3
"""Mirror Signalserver documentation and maintain translated copies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


LINK_TARGET_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML_TARGET_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")


class TranslationError(RuntimeError):
    """Raised when a translation cannot be generated safely."""


class Translator(Protocol):
    def translate(self, source: str, path: str, language: str, glossary: str) -> str:
        """Translate one source document."""


@dataclass(frozen=True)
class SyncResult:
    translated: int
    removed: int
    source_files: int


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def file_hash(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(value, ensure_ascii=False, indent=4, sort_keys=True) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(rendered, encoding="utf-8")
    temporary.replace(path)


def extract_fenced_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] | None = None
    closing_marker = ""

    for line in markdown.splitlines(keepends=True):
        marker_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if current is None:
            if marker_match:
                current = [line]
                closing_marker = marker_match.group(1)[0]
        else:
            current.append(line)
            if re.match(
                rf"^\s*{re.escape(closing_marker)}{{3,}}"
                rf"[ \t]*(?:<!--.*-->|-->)?[ \t]*(?:\n)?$",
                line,
            ):
                blocks.append("".join(current))
                current = None
                closing_marker = ""

    if current is not None:
        blocks.append("".join(current))

    return blocks


def protected_markdown_parts(markdown: str) -> dict[str, list[str]]:
    return {
        "fenced code blocks": [
            block.rstrip() for block in extract_fenced_blocks(markdown)
        ],
        "inline code": INLINE_CODE_RE.findall(markdown),
        "Markdown link targets": LINK_TARGET_RE.findall(markdown),
        "HTML link targets": HTML_TARGET_RE.findall(markdown),
    }


def validate_translation(source: str, translated: str) -> list[str]:
    errors: list[str] = []
    if not translated.strip():
        return ["translation is empty"]

    source_parts = protected_markdown_parts(source)
    translated_parts = protected_markdown_parts(translated)
    for label, expected in source_parts.items():
        actual = translated_parts[label]
        if actual != expected:
            errors.append(f"{label} changed")

    return errors


def strip_outer_markdown_fence(value: str) -> str:
    stripped = value.strip()
    match = re.fullmatch(r"```(?:markdown|md)?\s*\n(.*)\n```", stripped, re.DOTALL)
    return match.group(1) if match else value.strip()


class OpenAITranslator:
    def __init__(self, model: str, prompt_version: str) -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise TranslationError("OPENAI_API_KEY is required when translations are pending")

        try:
            from openai import OpenAI
        except ImportError as error:
            raise TranslationError("Install dependencies from requirements.txt") from error

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.prompt_version = prompt_version

    def translate(self, source: str, path: str, language: str, glossary: str) -> str:
        instructions = f"""You translate technical product documentation from English to {language}.
Return only the complete translated document, without commentary or an enclosing code fence.
Preserve the Markdown structure, whitespace where structurally meaningful, HTML, code fences,
code samples, inline code, commands, filenames, identifiers, URLs, link destinations, image paths,
and Docsify syntax exactly. Translate visible prose and link labels naturally and consistently.
Do not add, remove, summarize, or reinterpret information. This is prompt version {self.prompt_version}.

Terminology glossary:
{glossary}
"""

        previous_errors: list[str] = []
        for attempt in range(1, 4):
            retry_note = ""
            if previous_errors:
                retry_note = (
                    "\nThe previous attempt was rejected because: "
                    + "; ".join(previous_errors)
                    + ". Correct these issues.\n"
                )

            response = self.client.responses.create(
                model=self.model,
                instructions=instructions,
                input=f"File: {path}{retry_note}\n\n{source}",
            )
            translated = strip_outer_markdown_fence(response.output_text)
            previous_errors = validate_translation(source, translated)
            if not previous_errors:
                return translated.rstrip() + "\n"

        raise TranslationError(
            f"Translation of {path} failed validation after 3 attempts: "
            + "; ".join(previous_errors)
        )


def iter_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
    }


def remove_empty_directories(root: Path) -> None:
    if not root.exists():
        return
    for directory in sorted(
        (path for path in root.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass


def sync_files(files: dict[str, Path], destination: Path) -> int:
    destination.mkdir(parents=True, exist_ok=True)
    removed = 0

    for relative_path, source_path in files.items():
        target_path = destination / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        if not target_path.exists() or file_hash(source_path) != file_hash(target_path):
            shutil.copy2(source_path, target_path)

    expected = set(files)
    for relative_path, target_path in iter_files(destination).items():
        if relative_path not in expected:
            target_path.unlink()
            removed += 1

    remove_empty_directories(destination)
    return removed


def synchronize(
    source: Path,
    repository: Path,
    config: dict,
    source_sha: str,
    translator: Translator | None = None,
) -> SyncResult:
    if not source.is_dir():
        raise TranslationError(f"Source directory does not exist: {source}")

    ignored = set(config["ignored_source_paths"])
    extensions = set(config["translatable_extensions"])
    all_source_files = {
        relative: path
        for relative, path in iter_files(source).items()
        if relative not in ignored
    }
    translatable = {
        relative: path
        for relative, path in all_source_files.items()
        if path.suffix.lower() in extensions
    }
    shared = {
        relative: path
        for relative, path in all_source_files.items()
        if relative not in translatable
    }

    state_path = repository / "translation/state.json"
    state = load_json(state_path)
    state.setdefault("version", 1)
    state.setdefault("languages", {})

    pending: dict[str, list[str]] = {}
    for language_code, language_config in config["languages"].items():
        glossary_path = repository / language_config["glossary"]
        glossary_hash = file_hash(glossary_path)
        language_state = state["languages"].setdefault(language_code, {})
        file_state = language_state.setdefault("files", {})
        destination = repository / "content" / language_code

        language_pending: list[str] = []
        for relative, source_path in translatable.items():
            source_hash = file_hash(source_path)
            translated_path = destination / relative
            recorded = file_state.get(relative, {})
            if (
                not translated_path.exists()
                or recorded.get("source_hash") != source_hash
                or recorded.get("prompt_version") != config["prompt_version"]
                or recorded.get("glossary_hash") != glossary_hash
                or recorded.get("translation_hash")
                != (file_hash(translated_path) if translated_path.exists() else None)
            ):
                language_pending.append(relative)

        pending[language_code] = language_pending

    if any(pending.values()) and translator is None:
        model = os.environ.get("OPENAI_MODEL", config["model"])
        translator = OpenAITranslator(model, config["prompt_version"])

    removed = sync_files(translatable, repository / "content/en")
    removed += sync_files(shared, repository / "shared")
    translated_count = 0

    for language_code, language_config in config["languages"].items():
        glossary_path = repository / language_config["glossary"]
        glossary = glossary_path.read_text(encoding="utf-8")
        glossary_hash = file_hash(glossary_path)
        language_state = state["languages"][language_code]
        file_state = language_state["files"]
        destination = repository / "content" / language_code
        destination.mkdir(parents=True, exist_ok=True)

        for relative in pending[language_code]:
            source_text = translatable[relative].read_text(encoding="utf-8")
            assert translator is not None
            translated_text = translator.translate(
                source_text,
                relative,
                language_config["english_name"],
                glossary,
            )
            errors = validate_translation(source_text, translated_text)
            if errors:
                raise TranslationError(
                    f"Translation of {relative} is invalid: " + "; ".join(errors)
                )

            translated_path = destination / relative
            translated_path.parent.mkdir(parents=True, exist_ok=True)
            translated_path.write_text(translated_text.rstrip() + "\n", encoding="utf-8")
            file_state[relative] = {
                "glossary_hash": glossary_hash,
                "prompt_version": config["prompt_version"],
                "source_hash": file_hash(translatable[relative]),
                "translation_hash": file_hash(translated_path),
            }
            translated_count += 1

        expected = set(translatable)
        for relative, translated_path in iter_files(destination).items():
            if relative not in expected:
                translated_path.unlink()
                removed += 1
        for relative in list(file_state):
            if relative not in expected:
                del file_state[relative]
        remove_empty_directories(destination)

        language_state.update(
            {
                "glossary_hash": glossary_hash,
                "name": language_config["name"],
                "prompt_version": config["prompt_version"],
            }
        )

    state["source"] = {
        "commit": source_sha,
        "path": config["source"]["path"],
        "repository": config["source"]["repository"],
    }
    write_json(state_path, state)

    return SyncResult(
        translated=translated_count,
        removed=removed,
        source_files=len(all_source_files),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--repository", default=Path.cwd(), type=Path)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument(
        "--config",
        default=Path("translation/config.json"),
        type=Path,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repository = args.repository.resolve()
    config_path = args.config
    if not config_path.is_absolute():
        config_path = repository / config_path
    config = load_json(config_path)

    try:
        result = synchronize(
            args.source.resolve(),
            repository,
            config,
            args.source_sha,
        )
    except TranslationError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(
        f"Synchronized {result.source_files} source files, "
        f"translated {result.translated}, removed {result.removed}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
