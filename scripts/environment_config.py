#!/usr/bin/env python3
"""Read and validate documentation environment configuration."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ENVIRONMENT_NAMES = ("testing", "staging", "production")


class EnvironmentConfigError(ValueError):
    """Raised when deployment/environments.json is invalid."""


def load_config(repository: Path) -> dict:
    path = repository / "deployment/environments.json"
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise EnvironmentConfigError(f"missing environment config: {path}") from error
    except json.JSONDecodeError as error:
        raise EnvironmentConfigError(f"invalid environment config JSON: {error}") from error

    errors = validate_config(config)
    if errors:
        raise EnvironmentConfigError("; ".join(errors))
    return config


def validate_config(config: dict) -> list[str]:
    errors: list[str] = []
    if config.get("version") != 1:
        errors.append("version must be 1")

    environments = config.get("environments")
    if not isinstance(environments, dict):
        return [*errors, "environments must be an object"]

    unknown = set(environments) - set(ENVIRONMENT_NAMES)
    if unknown:
        errors.append(f"unknown environments: {', '.join(sorted(unknown))}")

    for name in ENVIRONMENT_NAMES:
        environment = environments.get(name)
        if not isinstance(environment, dict):
            errors.append(f"{name} configuration is missing")
            continue

        enabled = environment.get("enabled")
        auto_deploy = environment.get("auto_deploy")
        source_ref = environment.get("source_ref")
        if not isinstance(enabled, bool):
            errors.append(f"{name}.enabled must be a boolean")
        if not isinstance(auto_deploy, bool):
            errors.append(f"{name}.auto_deploy must be a boolean")
        if source_ref is not None and (
            not isinstance(source_ref, str) or not source_ref.strip()
        ):
            errors.append(f"{name}.source_ref must be a non-empty string or null")
        if enabled and not source_ref:
            errors.append(f"{name}.source_ref is required when enabled")
        if auto_deploy and not enabled:
            errors.append(f"{name}.auto_deploy requires enabled=true")

    return errors


def get_environment(config: dict, name: str) -> dict:
    if name not in ENVIRONMENT_NAMES:
        raise EnvironmentConfigError(f"unsupported environment: {name}")
    return config["environments"][name]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("environment", nargs="?", choices=ENVIRONMENT_NAMES)
    parser.add_argument(
        "--require-enabled",
        action="store_true",
        help="Fail when the selected environment is disabled.",
    )
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="Print values in GitHub Actions output format.",
    )
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]

    try:
        config = load_config(repository)
        if arguments.environment is None:
            print("Environment configuration is valid.")
            return 0

        environment = get_environment(config, arguments.environment)
        if arguments.require_enabled and not environment["enabled"]:
            raise EnvironmentConfigError(
                f"{arguments.environment} documentation deployment is disabled"
            )

        if arguments.github_output:
            print(f"enabled={str(environment['enabled']).lower()}")
            print(f"auto_deploy={str(environment['auto_deploy']).lower()}")
            print(f"source_ref={environment['source_ref'] or ''}")
        else:
            print(json.dumps(environment, indent=4, sort_keys=True))
        return 0
    except EnvironmentConfigError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
