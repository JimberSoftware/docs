from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_site import build
from scripts.sync_docs import (
    restore_protected_markdown,
    synchronize,
    validate_translation,
)


class FakeTranslator:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def translate(self, source: str, path: str, language: str, glossary: str) -> str:
        self.calls.append(path)
        return source.replace("Hello", "Bonjour")


class SyncDocsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.source = root / "source"
        self.repository = root / "repository"
        self.source.mkdir()
        (self.repository / "translation/glossaries").mkdir(parents=True)
        (self.repository / "translation/glossaries/fr.md").write_text(
            "Hello: Bonjour\n",
            encoding="utf-8",
        )
        (self.repository / "translation/state.json").write_text(
            '{"version": 1, "source": {}, "languages": {}}\n',
            encoding="utf-8",
        )
        self.config = {
            "source": {"repository": "source/repo", "path": "apps/docs"},
            "model": "test-model",
            "prompt_version": "1",
            "translatable_extensions": [".md"],
            "ignored_source_paths": ["index.html"],
            "languages": {
                "fr": {
                    "name": "Français",
                    "english_name": "French",
                    "glossary": "translation/glossaries/fr.md",
                }
            },
        }

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_synchronizes_and_only_retranslates_changed_documents(self) -> None:
        (self.source / "README.md").write_text(
            "# Hello\n\n[Link](guide.md) and `value`.\n",
            encoding="utf-8",
        )
        (self.source / "logo.png").write_bytes(b"image")
        translator = FakeTranslator()

        first = synchronize(
            self.source,
            self.repository,
            self.config,
            "abc123",
            translator,
        )
        second = synchronize(
            self.source,
            self.repository,
            self.config,
            "abc123",
            translator,
        )

        self.assertEqual(first.translated, 1)
        self.assertEqual(second.translated, 0)
        self.assertEqual(translator.calls, ["README.md"])
        self.assertEqual(
            (self.repository / "content/fr/README.md").read_text(encoding="utf-8"),
            "# Bonjour\n\n[Link](guide.md) and `value`.\n",
        )
        self.assertEqual((self.repository / "shared/logo.png").read_bytes(), b"image")

        state = json.loads(
            (self.repository / "translation/state.json").read_text(encoding="utf-8")
        )
        self.assertEqual(state["source"]["commit"], "abc123")

    def test_removes_deleted_documents_and_assets(self) -> None:
        (self.source / "README.md").write_text("Hello\n", encoding="utf-8")
        (self.source / "old.png").write_bytes(b"old")
        translator = FakeTranslator()
        synchronize(self.source, self.repository, self.config, "one", translator)

        (self.source / "README.md").unlink()
        (self.source / "old.png").unlink()
        result = synchronize(self.source, self.repository, self.config, "two", translator)

        self.assertGreaterEqual(result.removed, 3)
        self.assertFalse((self.repository / "content/en/README.md").exists())
        self.assertFalse((self.repository / "content/fr/README.md").exists())
        self.assertFalse((self.repository / "shared/old.png").exists())

    def test_validation_rejects_changed_protected_markdown(self) -> None:
        source = "See [guide](guide.md), use `command`.\n\n```sh\necho ok\n```\n"
        translated = "Voir [guide](guide-fr.md), utilisez `commande`.\n\n```sh\necho non\n```\n"

        errors = validate_translation(source, translated)

        self.assertIn("fenced code blocks changed", errors)
        self.assertIn("inline code changed", errors)
        self.assertIn("Markdown link targets changed", errors)

    def test_restores_code_and_link_targets_after_translation(self) -> None:
        source = (
            "Run `command` and read [the guide](guide.md).\n\n"
            "```sh\necho ok\n```\n"
        )
        translated = (
            "Exécutez `commande` et lisez [le guide](guide-fr.md).\n\n"
            "```sh\necho non\n```\n"
        )

        restored = restore_protected_markdown(source, translated)

        self.assertEqual(validate_translation(source, restored), [])
        self.assertIn("Exécutez", restored)
        self.assertIn("`command`", restored)
        self.assertIn("(guide.md)", restored)
        self.assertIn("echo ok", restored)

    def test_site_localizes_root_absolute_urls_at_render_time(self) -> None:
        (self.repository / "content/en").mkdir(parents=True)
        (self.repository / "content/fr").mkdir(parents=True)
        for language in ("en", "fr"):
            (self.repository / f"content/{language}/README.md").write_text(
                "# Documentation\n",
                encoding="utf-8",
            )
        (self.repository / "translation/config.json").write_text(
            json.dumps(self.config),
            encoding="utf-8",
        )

        output = build(self.repository)
        french_index = (output / "fr/index.html").read_text(encoding="utf-8")

        self.assertIn("return documentationBasePath + '/fr' + url", french_index)
        self.assertIn('const supportedLanguages = ["en", "fr"]', french_index)


if __name__ == "__main__":
    unittest.main()
