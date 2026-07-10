#!/usr/bin/env python3
"""Regression tests for the skill package validator."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).with_name("validate-skills.py")
SPEC = importlib.util.spec_from_file_location("validate_skills", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

markdown_table_rows = VALIDATOR.markdown_table_rows
validate_eval_cases = VALIDATOR.validate_eval_cases
validate_local_links = VALIDATOR.validate_local_links
validate_repository_indexes = VALIDATOR.validate_repository_indexes


VALID_EVAL = """# Eval Cases

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `one` | Trigger. |
| `two` | Trigger. |
| `three` | Trigger. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `four` | Prefer another skill. |
| `five` | Prefer another skill. |
| `six` | Prefer another skill. |

## Quality Eval

| Case | Pass | Reject If |
| --- | --- | --- |
| A | Evidence A | Failure A |
| B | Evidence B | Failure B |
| C | Evidence C | Failure C |
| D | Evidence D | Failure D |

## Scoring

Minimum pass: every quality case scores at least 7.
"""


class ValidateSkillsTests(unittest.TestCase):
    def test_repository_indexes_must_match_source_packages(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            packages = [
                VALIDATOR.SkillPackage(name="alpha", path=root / "skills" / "alpha"),
                VALIDATOR.SkillPackage(name="beta", path=root / "skills" / "beta"),
            ]
            (root / "README.md").write_text(
                "| `alpha` | First |\n| `beta` | Second |\n", encoding="utf-8"
            )
            (root / "INSTALL.md").write_text(
                "- `skills/alpha`\n- `skills/beta`\n", encoding="utf-8"
            )
            (root / "skills.sh.json").write_text(
                '{"groupings":[{"skills":["alpha","beta"]}]}', encoding="utf-8"
            )

            self.assertEqual([], validate_repository_indexes(root, packages))

            (root / "skills.sh.json").write_text(
                '{"groupings":[{"skills":["alpha","gamma"]}]}', encoding="utf-8"
            )
            errors = validate_repository_indexes(root, packages)

        self.assertTrue(any("missing skill beta" in error for error in errors))
        self.assertTrue(any("unknown skill gamma" in error for error in errors))

    def test_legacy_regex_catches_retired_skill_names(self) -> None:
        for name in (
            "frontend-implementation",
            "frontend-governance",
            "rust-engineering-governance",
        ):
            self.assertIsNotNone(VALIDATOR.LEGACY_RE.search(f"use {name} now"))

    def test_markdown_table_rows_returns_data_only(self) -> None:
        rows = markdown_table_rows(VALID_EVAL, "## Trigger Eval")
        self.assertEqual(3, len(rows))
        self.assertEqual(["`one`", "Trigger."], rows[0])

    def test_eval_validation_accepts_minimum_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            eval_file = Path(temp_dir) / "eval-cases.md"
            eval_file.write_text(VALID_EVAL, encoding="utf-8")
            errors, metrics = validate_eval_cases(eval_file, label="test")

        self.assertEqual([], errors)
        self.assertIsNotNone(metrics)
        self.assertEqual(3, metrics.trigger_cases)
        self.assertEqual(4, metrics.quality_cases)

    def test_eval_validation_rejects_duplicates_and_weak_scoring(self) -> None:
        invalid_eval = VALID_EVAL.replace("`two`", "`one`").replace("at least 7", "at least 5")
        with tempfile.TemporaryDirectory() as temp_dir:
            eval_file = Path(temp_dir) / "eval-cases.md"
            eval_file.write_text(invalid_eval, encoding="utf-8")
            errors, _ = validate_eval_cases(eval_file, label="test")

        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("score" in error for error in errors))

    def test_local_link_validation_rejects_missing_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package = Path(temp_dir) / "sample-skill"
            package.mkdir()
            (package / "SKILL.md").write_text("[missing](references/missing.md)\n", encoding="utf-8")

            errors = validate_local_links(package, label="test")

        self.assertEqual(1, len(errors))
        self.assertIn("broken local link", errors[0])


if __name__ == "__main__":
    unittest.main()
