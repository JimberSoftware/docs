import tempfile
import unittest
from pathlib import Path

from scripts.build_site import build, normalize_base_path


class BuildSiteTests(unittest.TestCase):
    def test_normalizes_documentation_base_path(self) -> None:
        self.assertEqual(normalize_base_path("documentation/"), "/documentation")
        self.assertEqual(normalize_base_path("/"), "")

    def test_build_uses_deployment_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository = Path(temporary_directory)
            (repository / "translation").mkdir()
            (repository / "translation/config.json").write_text(
                '{"languages":{"fr":{"name":"Français"}}}',
                encoding="utf-8",
            )
            (repository / "content/en").mkdir(parents=True)
            (repository / "content/fr").mkdir(parents=True)
            (repository / "content/en/README.md").write_text("English", encoding="utf-8")
            (repository / "content/fr/README.md").write_text("Français", encoding="utf-8")

            output = build(repository, "/documentation")

            root_index = (output / "index.html").read_text(encoding="utf-8")
            french_index = (output / "fr/index.html").read_text(encoding="utf-8")
            self.assertIn("'/documentation/' + language", root_index)
            self.assertIn("const documentationBasePath = '/documentation'", french_index)
            self.assertIn("documentationBasePath + '/fr/'", french_index)
            self.assertIn('class="sidebar-header"', french_index)
            self.assertIn("sidebar.insertBefore(header, sidebar.firstChild)", french_index)
            self.assertIn("namespace: 'jimber-sase-documentation-fr'", french_index)
            self.assertIn("Rechercher dans la documentation", french_index)
            self.assertIn("new MutationObserver(cleanSearchResults)", french_index)
            self.assertIn("if (cleanedText !== element.textContent)", french_index)
            self.assertIn(".matching-post h2, .matching-post p", french_index)


if __name__ == "__main__":
    unittest.main()
