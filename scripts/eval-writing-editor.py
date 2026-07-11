#!/usr/bin/env python3
"""Run deterministic Writing Editor behavior fixtures.

These fixtures test whether a candidate output preserves explicit source
contracts. They do not execute or grade an LLM and must not be reported as a
complete writing-quality evaluation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURES = ROOT / "skills/writing-editor/references/behavior-eval-fixtures.json"


@dataclass(frozen=True)
class Result:
    case_id: str
    passed: bool
    failures: tuple[str, ...]


def evaluate_case(case: dict[str, object]) -> Result:
    output = str(case["output"])
    failures: list[str] = []

    for value in case.get("must_contain", []):
        if str(value) not in output:
            failures.append(f"missing required text: {value!r}")
    for value in case.get("must_not_contain", []):
        if str(value) in output:
            failures.append(f"contains rejected text: {value!r}")
    for group in case.get("must_contain_one_of", []):
        alternatives = [str(value) for value in group]
        if not any(value in output for value in alternatives):
            failures.append(f"missing one of: {alternatives!r}")

    actual_pass = not failures
    expected_pass = bool(case["expected_pass"])
    if actual_pass != expected_pass:
        expectation = "pass" if expected_pass else "fail"
        failures.append(f"fixture was expected to {expectation}")
        return Result(str(case["id"]), False, tuple(failures))
    return Result(str(case["id"]), True, ())


def load_fixtures(path: Path) -> list[dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("fixture root must be a list")
    return data


def run_fixtures(path: Path) -> list[Result]:
    return [evaluate_case(case) for case in load_fixtures(path)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    args = parser.parse_args()

    results = run_fixtures(args.fixtures)
    failed = [result for result in results if not result.passed]
    for result in failed:
        print(f"FAIL {result.case_id}: {'; '.join(result.failures)}")
    print(f"Writing Editor behavior fixtures: {len(results) - len(failed)}/{len(results)} passed")
    print("Scope: deterministic contract fixtures only; LLM execution and subjective prose quality are not verified.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
