#!/usr/bin/env python3
"""Focused regression tests for the ui-spec v2 artifact validator."""

from __future__ import annotations

import hashlib
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
import venv
from unittest import mock
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ui-spec" / "scripts" / "validate_ui_spec.py"
TEMPLATES = ROOT / "skills" / "ui-spec" / "assets" / "templates"
SPEC = importlib.util.spec_from_file_location("validate_ui_spec", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class UiSpecValidatorTests(unittest.TestCase):
    def make_package(self) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        package = Path(temporary.name) / "package"
        shutil.copytree(TEMPLATES, package)
        return package

    def make_repository_package(self) -> tuple[Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repository = Path(temporary.name) / "repository"
        package = repository / ".codex" / "artifacts" / "surface-specification"
        package.parent.mkdir(parents=True)
        shutil.copytree(TEMPLATES, package)
        return repository, package

    @staticmethod
    def load_yaml(package: Path, name: str) -> dict:
        return yaml.safe_load((package / name).read_text(encoding="utf-8"))

    @staticmethod
    def write_yaml(package: Path, name: str, document: dict) -> None:
        (package / name).write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")

    def refresh_hashes(self, package: Path, repository_root: Path | None = None) -> None:
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        profile = self.load_yaml(package, "profile.yaml")
        durable = profile.get("durable_shared", {}).get("root")
        for output in manifest["outputs"].values():
            base = package if output["root"] == "task-local" else repository_root / durable
            output["sha256"] = hashlib.sha256((base / output["path"]).read_bytes()).hexdigest()
        self.write_yaml(package, "artifact-manifest.yaml", manifest)

    def mark_accepted(self, package: Path) -> None:
        evaluation = self.load_yaml(package, "evaluation.yaml")
        evaluation.update({"scores": {"product_truth": 15, "source_fidelity": 15, "information_architecture": 10, "interaction_states": 15, "responsive_accessibility": 15, "component_token_mapping": 15, "engineering_fit": 10, "evidence": 5}, "total": 100, "status": "accepted", "decision": "accepted"})
        self.write_yaml(package, "evaluation.yaml", evaluation)
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["evaluation"] = {"score": 100, "status": "accepted"}
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.refresh_hashes(package)

    def test_templates_are_valid_and_hash_real_files(self) -> None:
        self.assertEqual([], VALIDATOR.validate(self.make_package()))

    def test_v1_is_a_stable_migration_error(self) -> None:
        package = self.make_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["version"] = 1
        self.write_yaml(package, "profile.yaml", profile)
        self.assertEqual(["V1_MIGRATION_REQUIRED: migrate all package documents and manifest outputs to schema v2"], VALIDATOR.validate(package))

    def test_schema_rejects_nested_wrong_types_and_unknown_fields(self) -> None:
        package = self.make_package()
        task = self.load_yaml(package, "task.yaml")
        task["task"]["id"] = None
        task["unexpected"] = True
        self.write_yaml(package, "task.yaml", task)
        errors = VALIDATOR.validate(package)
        self.assertTrue(any("task.yaml.task.id" in error for error in errors))
        self.assertTrue(any("task.yaml" in error and "unexpected" in error for error in errors))

    def test_cross_document_revisions_are_bound(self) -> None:
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["inputs"]["tokens_revision"] = 2
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertIn("SEMANTIC_ERROR inputs.tokens_revision: differs from design-tokens.json.revision", VALIDATOR.validate(package))

    def test_output_hash_missing_file_and_directory_fail(self) -> None:
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["profile"]["sha256"] = "0" * 64
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("does not match file" in error for error in VALIDATOR.validate(package)))
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["profile"]["path"] = "missing.yaml"
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("file does not exist" in error for error in VALIDATOR.validate(package)))

    def test_output_paths_reject_escape_forms(self) -> None:
        for unsafe in ("../secret", "/private/tmp/file", "C:\\temp\\file", "//server/share", "folder/../file"):
            with self.subTest(unsafe=unsafe):
                package = self.make_package()
                manifest = self.load_yaml(package, "artifact-manifest.yaml")
                manifest["outputs"]["profile"]["path"] = unsafe
                self.write_yaml(package, "artifact-manifest.yaml", manifest)
                self.assertTrue(any("safe relative POSIX" in error for error in VALIDATOR.validate(package)))

    def test_durable_output_requires_safe_root_and_exact_approval(self) -> None:
        repository, package = self.make_repository_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["durable_shared"] = {"root": "docs/design-system"}
        self.write_yaml(package, "profile.yaml", profile)
        target = repository / "docs/design-system" / "tokens.json"
        target.parent.mkdir(parents=True)
        target.write_text("{}\n", encoding="utf-8")
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["tokens"] = {"root": "durable-shared", "path": "tokens.json", "sha256": digest, "approval_ref": "promotion-1"}
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("requires repository_root" in error for error in VALIDATOR.validate(package)))
        self.assertTrue(any("exact approved sanitized" in error for error in VALIDATOR.validate(package, repository)))
        evaluation = self.load_yaml(package, "evaluation.yaml")
        evaluation["promotion_approvals"] = [{"id": "promotion-1", "status": "approved", "sanitized": True, "output": "tokens", "root": "durable-shared", "path": "tokens.json", "sha256": digest}]
        self.write_yaml(package, "evaluation.yaml", evaluation)
        self.refresh_hashes(package, repository)
        self.assertEqual([], VALIDATOR.validate(package, repository))

    def test_accepted_requires_manifest_approval(self) -> None:
        package = self.make_package()
        self.mark_accepted(package)
        self.assertTrue(any("accepted requires approved_by" in error for error in VALIDATOR.validate(package)))
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["approval"] = {"approved_by": "design-owner", "approved_at": "2026-07-22T10:00:00+08:00"}
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertEqual([], VALIDATOR.validate(package))

    def test_error_order_is_deterministic(self) -> None:
        package = self.make_package()
        task = self.load_yaml(package, "task.yaml")
        task["unexpected"] = True
        task["task"]["id"] = None
        self.write_yaml(package, "task.yaml", task)
        self.assertEqual(VALIDATOR.validate(package), VALIDATOR.validate(package))

    def test_all_six_output_bindings_are_required_and_unique(self) -> None:
        for name in ("profile", "references", "task", "tokens", "component_map", "evaluation"):
            with self.subTest(name=name):
                package = self.make_package()
                manifest = self.load_yaml(package, "artifact-manifest.yaml")
                del manifest["outputs"][name]
                self.write_yaml(package, "artifact-manifest.yaml", manifest)
                self.assertTrue(any("artifact-manifest.yaml.outputs" in error for error in VALIDATOR.validate(package)))
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["references"] = dict(manifest["outputs"]["profile"])
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("duplicates logical target" in error for error in VALIDATOR.validate(package)))

    def test_changed_output_with_old_hash_fails(self) -> None:
        package = self.make_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["density"] = "changed-density"
        self.write_yaml(package, "profile.yaml", profile)
        self.assertTrue(any("outputs.profile.sha256" in error for error in VALIDATOR.validate(package)))

    def test_manifest_evaluation_and_rubric_are_bound(self) -> None:
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["evaluation"]["score"] = 1
        manifest["evaluation"]["status"] = "accepted"
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        errors = VALIDATOR.validate(package)
        self.assertTrue(any("manifest.evaluation.score" in error for error in errors))
        self.assertTrue(any("manifest.evaluation.status" in error for error in errors))
        package = self.make_package()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["inputs"]["rubric_revision"] = 2
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("rubric_revision" in error for error in VALIDATOR.validate(package)))

    def test_required_non_empty_boundaries_fail(self) -> None:
        package = self.make_package()
        task = self.load_yaml(package, "task.yaml")
        task["scope"]["exclude"] = []
        task["facts"]["unavailable"] = []
        self.write_yaml(package, "task.yaml", task)
        errors = VALIDATOR.validate(package)
        self.assertTrue(any("task.yaml.scope.exclude" in error for error in errors))
        self.assertTrue(any("task.yaml.facts.unavailable" in error for error in errors))
        package = self.make_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["visual_source"]["use"] = []
        self.write_yaml(package, "profile.yaml", profile)
        self.assertTrue(any("profile.yaml.visual_source.use" in error for error in VALIDATOR.validate(package)))
        for field in ("use", "ignore"):
            with self.subTest(reference_field=field):
                package = self.make_package()
                references = self.load_yaml(package, "references.yaml")
                references["references"][0][field] = []
                self.write_yaml(package, "references.yaml", references)
                self.assertTrue(any(f"references.yaml.references.0.{field}" in error for error in VALIDATOR.validate(package)))

    def test_output_paths_are_canonical_and_physical_targets_unique(self) -> None:
        for alias in ("a//b", "a/./b"):
            with self.subTest(alias=alias):
                package = self.make_package()
                manifest = self.load_yaml(package, "artifact-manifest.yaml")
                manifest["outputs"]["profile"]["path"] = alias
                self.write_yaml(package, "artifact-manifest.yaml", manifest)
                self.assertTrue(any("safe relative POSIX" in error for error in VALIDATOR.validate(package)))

        repository, package = self.make_repository_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["durable_shared"] = {"root": ".codex/artifacts/surface-specification"}
        self.write_yaml(package, "profile.yaml", profile)
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        digest = hashlib.sha256((package / "profile.yaml").read_bytes()).hexdigest()
        manifest["outputs"]["tokens"] = {"root": "durable-shared", "path": "profile.yaml", "sha256": digest, "approval_ref": "promotion-1"}
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        evaluation = self.load_yaml(package, "evaluation.yaml")
        evaluation["promotion_approvals"] = [{"id": "promotion-1", "status": "approved", "sanitized": True, "output": "tokens", "root": "durable-shared", "path": "profile.yaml", "sha256": digest}]
        self.write_yaml(package, "evaluation.yaml", evaluation)
        self.refresh_hashes(package, repository)
        self.assertTrue(any("duplicates physical target" in error for error in VALIDATOR.validate(package, repository)))

    def test_dependency_error_names_the_current_interpreter(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        environment = Path(temporary.name) / "venv"
        venv.EnvBuilder(with_pip=True).create(environment)
        interpreter = environment / "bin" / "python"
        result = subprocess.run(
            [str(interpreter), str(SCRIPT), "unused"], text=True, capture_output=True, check=False
        )
        self.assertEqual(1, result.returncode)
        self.assertIn(str(interpreter), result.stdout + result.stderr)
        self.assertIn("DEPENDENCY_ERROR", result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_accepted_bad_scores_and_output_read_errors_are_stable(self) -> None:
        package = self.make_package()
        self.mark_accepted(package)
        evaluation = self.load_yaml(package, "evaluation.yaml")
        del evaluation["scores"]["product_truth"]
        self.write_yaml(package, "evaluation.yaml", evaluation)
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(package)], text=True, capture_output=True, check=False
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("evaluation.scores", result.stdout)
        self.assertNotIn("Traceback", result.stdout + result.stderr)
        package = self.make_package()
        with mock.patch.object(Path, "read_bytes", side_effect=OSError("gone")):
            errors = VALIDATOR.validate(package)
        self.assertTrue(any("unreadable file (OSError)" in error for error in errors))

    def test_selected_source_empty_and_boundary_items_fail(self) -> None:
        package = self.make_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["visual_source"] = {}
        self.write_yaml(package, "profile.yaml", profile)
        self.assertTrue(any("profile.yaml.visual_source" in error for error in VALIDATOR.validate(package)))
        package = self.make_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["visual_source"]["use"] = [None]
        self.write_yaml(package, "profile.yaml", profile)
        self.assertTrue(any("profile.yaml.visual_source.use.0" in error for error in VALIDATOR.validate(package)))

    def test_source_revision_mismatch_fails(self) -> None:
        package = self.make_package()
        task = self.load_yaml(package, "task.yaml")
        task["visual_source"]["revision"] = "different-revision"
        self.write_yaml(package, "task.yaml", task)
        self.assertIn(
            "SEMANTIC_ERROR visual_source.revision: profile.yaml and task.yaml differ",
            VALIDATOR.validate(package),
        )

    def test_accepted_approval_identity_and_timezone_are_required(self) -> None:
        invalid = ((" ", "2026-07-22T10:00:00+08:00"), ("design-owner", "2026-07-22T10:00:00"))
        for approved_by, approved_at in invalid:
            with self.subTest(approved_by=approved_by, approved_at=approved_at):
                package = self.make_package()
                self.mark_accepted(package)
                manifest = self.load_yaml(package, "artifact-manifest.yaml")
                manifest["approval"] = {"approved_by": approved_by, "approved_at": approved_at}
                self.write_yaml(package, "artifact-manifest.yaml", manifest)
                self.assertTrue(any("accepted requires approved_by" in error for error in VALIDATOR.validate(package)))

    def test_unsafe_task_ids_fail(self) -> None:
        for task_id in ("../../src", "/private/tmp/spec", "nested/spec"):
            with self.subTest(task_id=task_id):
                package = self.make_package()
                task = self.load_yaml(package, "task.yaml")
                task["task"]["id"] = task_id
                self.write_yaml(package, "task.yaml", task)
                self.assertIn("SEMANTIC_ERROR task.id: must be a lowercase kebab-case slug", VALIDATOR.validate(package))

    def test_score_keys_types_ranges_and_totals_fail(self) -> None:
        mutations = (("bonus", 1), ("product_truth", "15"), ("product_truth", 16))
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                package = self.make_package()
                evaluation = self.load_yaml(package, "evaluation.yaml")
                evaluation["scores"][key] = value
                self.write_yaml(package, "evaluation.yaml", evaluation)
                self.assertTrue(any("evaluation.scores" in error for error in VALIDATOR.validate(package)))
        package = self.make_package()
        evaluation = self.load_yaml(package, "evaluation.yaml")
        evaluation["total"] = 1
        self.write_yaml(package, "evaluation.yaml", evaluation)
        self.assertIn("SEMANTIC_ERROR evaluation.total: must equal weighted score sum", VALIDATOR.validate(package))

    def test_distinct_task_packages_are_isolated(self) -> None:
        repository, first = self.make_repository_package()
        second = repository / ".codex" / "artifacts" / "billing-flow-spec"
        shutil.copytree(TEMPLATES, second)
        first_task = self.load_yaml(first, "task.yaml")
        first_task["task"]["id"] = "account-settings-spec"
        self.write_yaml(first, "task.yaml", first_task)
        self.refresh_hashes(first)
        second_task = self.load_yaml(second, "task.yaml")
        second_task["task"]["id"] = "billing-flow-spec"
        self.write_yaml(second, "task.yaml", second_task)
        self.refresh_hashes(second)
        self.assertEqual([], VALIDATOR.validate(first, repository))
        self.assertEqual([], VALIDATOR.validate(second, repository))
        self.assertNotEqual(first, second)

    def test_malformed_yaml_returns_error_without_traceback(self) -> None:
        package = self.make_package()
        (package / "task.yaml").write_text("task: [\n", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(package)], text=True, capture_output=True, check=False
        )
        self.assertEqual(1, result.returncode)
        self.assertIn("DOCUMENT_ERROR task.yaml: invalid document", result.stdout)
        self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_directory_output_and_symlink_escape_fail(self) -> None:
        package = self.make_package()
        (package / "directory").mkdir()
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["profile"]["path"] = "directory"
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("regular non-symlink" in error for error in VALIDATOR.validate(package)))
        package = self.make_package()
        outside = package.parent / "outside"
        outside.mkdir()
        (outside / "escape.yaml").write_text("outside\n", encoding="utf-8")
        (package / "link").symlink_to(outside, target_is_directory=True)
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["profile"]["path"] = "link/escape.yaml"
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("escapes its declared root" in error for error in VALIDATOR.validate(package)))

    def test_durable_root_and_symlink_escape_fail(self) -> None:
        repository, package = self.make_repository_package()
        profile = self.load_yaml(package, "profile.yaml")
        profile["durable_shared"] = {"root": "../outside"}
        self.write_yaml(package, "profile.yaml", profile)
        manifest = self.load_yaml(package, "artifact-manifest.yaml")
        manifest["outputs"]["tokens"] = {"root": "durable-shared", "path": "tokens.json", "sha256": "0" * 64, "approval_ref": "promotion-1"}
        self.write_yaml(package, "artifact-manifest.yaml", manifest)
        self.assertTrue(any("durable_shared.root" in error for error in VALIDATOR.validate(package, repository)))

        profile["durable_shared"] = {"root": "docs/design-system"}
        self.write_yaml(package, "profile.yaml", profile)
        outside = repository / "outside"
        outside.mkdir()
        (outside / "tokens.json").write_text("outside\n", encoding="utf-8")
        durable = repository / "docs/design-system"
        durable.parent.mkdir(parents=True)
        durable.symlink_to(outside, target_is_directory=True)
        self.assertTrue(any("must not traverse a symlink" in error for error in VALIDATOR.validate(package, repository)))


if __name__ == "__main__":
    unittest.main()
