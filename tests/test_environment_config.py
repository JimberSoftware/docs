from __future__ import annotations

import unittest

from scripts.environment_config import get_environment, validate_config


class EnvironmentConfigTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = {
            "version": 1,
            "environments": {
                "testing": {
                    "enabled": True,
                    "source_ref": "development",
                    "auto_deploy": True,
                },
                "staging": {
                    "enabled": False,
                    "source_ref": None,
                    "auto_deploy": False,
                },
                "production": {
                    "enabled": False,
                    "source_ref": None,
                    "auto_deploy": False,
                },
            },
        }

    def test_accepts_testing_only_configuration(self) -> None:
        self.assertEqual(validate_config(self.config), [])
        self.assertEqual(
            get_environment(self.config, "testing")["source_ref"],
            "development",
        )

    def test_requires_source_ref_for_enabled_environment(self) -> None:
        self.config["environments"]["staging"]["enabled"] = True

        errors = validate_config(self.config)

        self.assertIn("staging.source_ref is required when enabled", errors)

    def test_rejects_auto_deploy_for_disabled_environment(self) -> None:
        self.config["environments"]["production"]["auto_deploy"] = True

        errors = validate_config(self.config)

        self.assertIn("production.auto_deploy requires enabled=true", errors)


if __name__ == "__main__":
    unittest.main()
