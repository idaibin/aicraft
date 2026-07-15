#!/usr/bin/env python3
"""Compare deterministic AICraft Skill discovery and entrypoint footprint."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Footprint:
    skills: int
    description_characters: int
    default_prompt_characters: int
    skill_lines: int


def yaml_scalar(text: str, key: str) -> str:
    match = re.search(rf"^\s*{re.escape(key)}\s*:\s*(.+)$", text, re.MULTILINE)
    if match is None:
        raise ValueError(f"missing YAML scalar {key!r}")
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def measure_package(skill_text: str, openai_text: str) -> tuple[int, int, int]:
    return (
        len(yaml_scalar(skill_text, "description")),
        len(yaml_scalar(openai_text, "default_prompt")),
        len(skill_text.splitlines()),
    )


def current_footprint(root: Path = ROOT) -> Footprint:
    measures = []
    for skill_path in sorted((root / "skills").glob("*/SKILL.md")):
        openai_path = skill_path.parent / "agents" / "openai.yaml"
        measures.append(
            measure_package(
                skill_path.read_text(encoding="utf-8"),
                openai_path.read_text(encoding="utf-8"),
            )
        )
    return Footprint(
        skills=len(measures),
        description_characters=sum(item[0] for item in measures),
        default_prompt_characters=sum(item[1] for item in measures),
        skill_lines=sum(item[2] for item in measures),
    )


def git_text(ref: str, path: str, *, root: Path = ROOT) -> str:
    completed = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ValueError(completed.stderr.strip() or f"cannot read {ref}:{path}")
    return completed.stdout


def revision_footprint(ref: str, root: Path = ROOT) -> Footprint:
    completed = subprocess.run(
        ["git", "ls-tree", "-d", "--name-only", f"{ref}:skills"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise ValueError(completed.stderr.strip() or f"cannot list {ref}:skills")
    skill_names = [line for line in completed.stdout.splitlines() if line]
    measures = [
        measure_package(
            git_text(ref, f"skills/{name}/SKILL.md", root=root),
            git_text(ref, f"skills/{name}/agents/openai.yaml", root=root),
        )
        for name in skill_names
    ]
    return Footprint(
        skills=len(measures),
        description_characters=sum(item[0] for item in measures),
        default_prompt_characters=sum(item[1] for item in measures),
        skill_lines=sum(item[2] for item in measures),
    )


def percent_change(before: int, after: int) -> float:
    return (after - before) / before if before else 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-ref", default="HEAD")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    before = revision_footprint(args.baseline_ref)
    after = current_footprint()
    payload = {
        "baseline_ref": args.baseline_ref,
        "baseline": asdict(before),
        "candidate": asdict(after),
        "change": {
            key: {
                "absolute": getattr(after, key) - getattr(before, key),
                "percent": percent_change(getattr(before, key), getattr(after, key)),
            }
            for key in (
                "description_characters",
                "default_prompt_characters",
                "skill_lines",
            )
        },
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print(f"baseline: {args.baseline_ref}; skills: {before.skills} -> {after.skills}")
    for key, label in (
        ("description_characters", "discovery descriptions"),
        ("default_prompt_characters", "OpenAI default prompts"),
        ("skill_lines", "SKILL.md entrypoint lines"),
    ):
        prior = getattr(before, key)
        current = getattr(after, key)
        change = percent_change(prior, current)
        print(f"{label}: {prior} -> {current} ({change:+.1%})")
    print("Scope: deterministic text footprint only; behavior and outcomes are not measured.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
