#!/usr/bin/env python3
"""Regression tests for the design-system automation manifest validator."""

from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ui-spec" / "scripts" / "validate_design_system_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_design_system_manifest", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class DesignSystemManifestValidatorTests(unittest.TestCase):
    def make_fixture(self) -> tuple[Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repository = Path(temporary.name) / "repository"
        design = repository / "docs" / "ui" / "DESIGN.md"
        tokens = repository / "generated" / "design-tokens.json"
        consumer = repository / "scripts" / "check-design-system.py"
        manifest = repository / "docs" / "ui" / "design-system" / "manifest.yaml"
        design.parent.mkdir(parents=True)
        tokens.parent.mkdir(parents=True)
        consumer.parent.mkdir(parents=True)
        manifest.parent.mkdir(parents=True)
        design.write_text("# Design\n\nApproved visual decisions.\n", encoding="utf-8")
        tokens.write_text('{"color.primary":"#123456"}\n', encoding="utf-8")
        consumer.write_text("# repository automation consumer\n", encoding="utf-8")
        document = {
            "version": 1,
            "role": "automation-contract",
            "consumer": {
                "id": "design-contract-check",
                "path": "scripts/check-design-system.py",
                "sha256": hashlib.sha256(consumer.read_bytes()).hexdigest(),
            },
            "semantic_authority": {
                "path": "docs/ui/DESIGN.md",
                "sha256": hashlib.sha256(design.read_bytes()).hexdigest(),
            },
            "bindings": [{
                "id": "design-tokens",
                "kind": "tokens",
                "path": "generated/design-tokens.json",
                "sha256": hashlib.sha256(tokens.read_bytes()).hexdigest(),
            }],
            "conflict_policy": "fail",
            "approval": {
                "design_revision": 1,
                "approved_by": "design-owner",
                "approved_at": "2026-07-23T10:00:00+08:00",
            },
        }
        manifest.write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")
        return repository, manifest

    @staticmethod
    def load(manifest: Path) -> dict:
        return yaml.safe_load(manifest.read_text(encoding="utf-8"))

    @staticmethod
    def write(manifest: Path, document: dict) -> None:
        manifest.write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")

    def test_valid_manifest_binds_authority_and_assets(self) -> None:
        repository, manifest = self.make_fixture()
        self.assertEqual([], VALIDATOR.validate(manifest, repository))

    def test_changed_design_authority_is_a_hard_conflict(self) -> None:
        repository, manifest = self.make_fixture()
        (repository / "docs/ui/DESIGN.md").write_text("changed\n", encoding="utf-8")
        self.assertIn(
            "AUTHORITY_CONFLICT semantic_authority.sha256: semantic authority has changed",
            VALIDATOR.validate(manifest, repository),
        )

    def test_changed_binding_is_a_hard_conflict(self) -> None:
        repository, manifest = self.make_fixture()
        (repository / "generated/design-tokens.json").write_text("{}\n", encoding="utf-8")
        self.assertIn(
            "BINDING_CONFLICT bindings.0.sha256: bound asset has changed",
            VALIDATOR.validate(manifest, repository),
        )

    def test_changed_consumer_is_a_hard_conflict(self) -> None:
        repository, manifest = self.make_fixture()
        (repository / "scripts/check-design-system.py").write_text("changed\n", encoding="utf-8")
        self.assertIn(
            "CONSUMER_CONFLICT consumer.sha256: automation consumer has changed",
            VALIDATOR.validate(manifest, repository),
        )

    def test_manifest_cannot_introduce_design_decisions(self) -> None:
        repository, manifest = self.make_fixture()
        document = self.load(manifest)
        document["visual_principles"] = ["manifest-owned-decision"]
        self.write(manifest, document)
        self.assertTrue(any("visual_principles" in error for error in VALIDATOR.validate(manifest, repository)))

    def test_role_conflict_policy_and_consumer_are_closed(self) -> None:
        for path, value in (
            (("role",), "semantic-authority"),
            (("conflict_policy",), "warn"),
            (("consumer", "id"), ""),
        ):
            with self.subTest(path=path):
                repository, manifest = self.make_fixture()
                document = self.load(manifest)
                target = document
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.write(manifest, document)
                self.assertTrue(VALIDATOR.validate(manifest, repository))

    def test_paths_and_approval_timestamp_are_strict(self) -> None:
        repository, manifest = self.make_fixture()
        document = self.load(manifest)
        document["semantic_authority"]["path"] = "../DESIGN.md"
        document["approval"]["approved_at"] = "2026-07-23T10:00:00"
        self.write(manifest, document)
        errors = VALIDATOR.validate(manifest, repository)
        self.assertTrue(any("safe repository-relative" in error for error in errors))
        self.assertTrue(any("timezone-aware" in error for error in errors))

    def test_duplicate_binding_ids_and_paths_fail(self) -> None:
        repository, manifest = self.make_fixture()
        document = self.load(manifest)
        duplicate = dict(document["bindings"][0])
        document["bindings"].append(duplicate)
        self.write(manifest, document)
        errors = VALIDATOR.validate(manifest, repository)
        self.assertTrue(any("duplicate binding id" in error for error in errors))
        self.assertTrue(any("duplicate consumer, authority, or binding path" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
