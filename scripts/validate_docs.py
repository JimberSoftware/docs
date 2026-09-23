#!/usr/bin/env python3
"""Validate mirrored and translated documentation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from scripts.sync_docs import file_hash, iter_files, validate_translation


def validate(repository: Path) -> list[str]:
    errors: list[str] = []
    config = json.loads(
        (repository / "translation/config.json").read_text(encoding="utf-8")
    )
    state = json.loads(
        (repository / "translation/state.json").read_text(encoding="utf-8")
    )
    english = iter_files(repository / "content/en")
    expected_paths = set(english)

    if not expected_paths:
        errors.append("content/en contains no documents")

    for language_code in config["languages"]:
        translated = iter_files(repository / "content" / language_code)
        translated_paths = set(translated)
        missing = expected_paths - translated_paths
        extra = translated_paths - expected_paths
        if missing:
            errors.append(f"{language_code} is missing: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{language_code} has unexpected files: {', '.join(sorted(extra))}")

        language_state = state.get("languages", {}).get(language_code, {})
        file_state = language_state.get("files", {})
        for relative in sorted(expected_paths & translated_paths):
            source_path = english[relative]
            translated_path = translated[relative]
            recorded = file_state.get(relative)
            if recorded is None:
                errors.append(f"{language_code}/{relative} has no translation state")
                continue
            if recorded.get("source_hash") != file_hash(source_path):
                errors.append(f"{language_code}/{relative} has a stale source hash")
            if recorded.get("translation_hash") != file_hash(translated_path):
                errors.append(f"{language_code}/{relative} was changed outside automation")

            structural_errors = validate_translation(
                source_path.read_text(encoding="utf-8"),
                translated_path.read_text(encoding="utf-8"),
            )
            errors.extend(
                f"{language_code}/{relative}: {error}"
                for error in structural_errors
            )

    return errors


def main() -> int:
    repository = Path(__file__).resolve().parents[1]
    errors = validate(repository)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

