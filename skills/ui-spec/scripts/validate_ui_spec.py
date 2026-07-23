#!/usr/bin/env python3
"""Validate a versioned UI specification package without trusting manifest paths."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator, SchemaError
except ImportError as error:  # pragma: no cover - dependency boundary
    raise SystemExit(
        "DEPENDENCY_ERROR: run "
        f"`{shlex.quote(sys.executable)} -m pip install 'PyYAML==6.0.2' 'jsonschema==4.25.1'`"
    ) from error


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "assets" / "ui-spec-package.schema.json"
FILES = (
    "profile.yaml", "references.yaml", "task.yaml", "design-tokens.json",
    "component-map.json", "evaluation.yaml", "artifact-manifest.yaml",
)
RUBRIC_REVISION = 1
SCORE_MAXIMA = {"product_truth": 15, "source_fidelity": 15, "information_architecture": 10,
                "interaction_states": 15, "responsive_accessibility": 15,
                "component_token_mapping": 15, "engineering_fit": 10, "evidence": 5}
CORE_SCORE_KEYS = tuple(key for key, maximum in SCORE_MAXIMA.items() if maximum == 15)
SAFE_TASK_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_OUTPUTS = {
    "profile": "profile.yaml",
    "references": "references.yaml",
    "task": "task.yaml",
    "tokens": "design-tokens.json",
    "component_map": "component-map.json",
    "evaluation": "evaluation.yaml",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.suffix == ".json" else yaml.safe_load(path.read_text(encoding="utf-8"))


def missing(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        return datetime.fromisoformat(value.strip().replace("Z", "+00:00")).tzinfo is not None
    except ValueError:
        return False


def safe_relative(value: str) -> bool:
    if "\x00" in value or "\\" in value or value.startswith("//") or re.match(r"^[A-Za-z]:", value):
        return False
    path = PurePosixPath(value)
    return (
        bool(value)
        and str(path) == value
        and not path.is_absolute()
        and all(part not in ("", ".", "..") for part in path.parts)
    )


def resolve_inside(base: Path, relative: str) -> Path | None:
    if not safe_relative(relative):
        return None
    candidate = base / PurePosixPath(relative)
    try:
        candidate.resolve(strict=False).relative_to(base.resolve(strict=False))
    except ValueError:
        return None
    return candidate


def traverses_symlink(base: Path, candidate: Path) -> bool:
    try:
        relative = candidate.relative_to(base)
    except ValueError:
        return True
    current = base
    if current.is_symlink():
        return True
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            return True
    return False


def schema_errors(documents: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(documents), key=lambda item: (tuple(map(str, item.absolute_path)), item.message)):
        location = ".".join(str(part) for part in error.absolute_path) or "package"
        errors.append(f"SCHEMA_ERROR {location}: {error.message}")
    return errors


def semantic_errors(
    root: Path, docs: dict[str, Any], repository_root: Path | None = None
) -> list[str]:
    errors: list[str] = []
    profile, task, evaluation, manifest = (docs[name] for name in ("profile.yaml", "task.yaml", "evaluation.yaml", "artifact-manifest.yaml"))
    for key in ("id", "revision", "status", "source", "rights_status", "use", "ignore"):
        if profile["visual_source"][key] != task["visual_source"][key]:
            errors.append(f"SEMANTIC_ERROR visual_source.{key}: profile.yaml and task.yaml differ")
    task_id = task["task"]["id"]
    if not SAFE_TASK_ID.fullmatch(task_id):
        errors.append("SEMANTIC_ERROR task.id: must be a lowercase kebab-case slug")
    source = manifest["source"]
    if source["visual_source_id"] != profile["visual_source"]["id"]:
        errors.append("SEMANTIC_ERROR source.visual_source_id: differs from profile/task")
    if source["visual_source_revision"] != profile["visual_source"]["revision"]:
        errors.append("SEMANTIC_ERROR source.visual_source_revision: differs from profile/task")
    bindings = {"profile_revision": "profile.yaml", "task_revision": "task.yaml", "reference_revision": "references.yaml", "tokens_revision": "design-tokens.json", "component_map_revision": "component-map.json", "evaluation_revision": "evaluation.yaml"}
    for field, filename in bindings.items():
        if manifest["inputs"][field] != docs[filename]["revision"]:
            errors.append(f"SEMANTIC_ERROR inputs.{field}: differs from {filename}.revision")
    if manifest["inputs"]["rubric_revision"] != RUBRIC_REVISION:
        errors.append("SEMANTIC_ERROR inputs.rubric_revision: differs from validator rubric revision")
    if manifest["evaluation"]["score"] != evaluation["total"]:
        errors.append("SEMANTIC_ERROR manifest.evaluation.score: differs from evaluation.yaml.total")
    if manifest["evaluation"]["status"] != evaluation["status"]:
        errors.append("SEMANTIC_ERROR manifest.evaluation.status: differs from evaluation.yaml.status")

    shared_root = profile.get("durable_shared", {}).get("root")
    if shared_root is not None and not safe_relative(shared_root):
        errors.append("SEMANTIC_ERROR profile.durable_shared.root: must be a safe repository-relative path")
    approvals = {item["id"]: item for item in evaluation["promotion_approvals"]}
    targets: set[tuple[str, str]] = set()
    physical_targets: dict[Path, str] = {}
    for name in REQUIRED_OUTPUTS:
        output = manifest["outputs"][name]
        root_kind, relative, digest = output["root"], output["path"], output["sha256"]
        target_key = (root_kind, relative)
        if target_key in targets:
            errors.append(f"SEMANTIC_ERROR outputs.{name}: duplicates logical target {root_kind}/{relative}")
        targets.add(target_key)
        if not safe_relative(relative):
            errors.append(f"SEMANTIC_ERROR outputs.{name}.path: must be a safe relative POSIX path")
            continue
        if root_kind == "task-local":
            if "approval_ref" in output:
                errors.append(f"SEMANTIC_ERROR outputs.{name}.approval_ref: task-local output cannot be promoted")
            base = root
            if relative != REQUIRED_OUTPUTS[name]:
                errors.append(f"SEMANTIC_ERROR outputs.{name}.path: task-local binding must be {REQUIRED_OUTPUTS[name]}")
        else:
            if repository_root is None:
                errors.append(f"SEMANTIC_ERROR outputs.{name}: durable-shared requires repository_root")
                continue
            if not shared_root or not safe_relative(shared_root):
                errors.append(f"SEMANTIC_ERROR outputs.{name}: durable-shared requires profile.durable_shared.root")
                continue
            if not output.get("approval_ref"):
                errors.append(f"SEMANTIC_ERROR outputs.{name}: durable-shared requires approval_ref")
            base = resolve_inside(repository_root, shared_root)
            if base is None:
                errors.append(f"SEMANTIC_ERROR outputs.{name}: durable-shared root escapes repository_root")
                continue
        target = resolve_inside(base, relative)
        if target is None:
            errors.append(f"SEMANTIC_ERROR outputs.{name}.path: escapes its declared root")
        elif traverses_symlink(base, target):
            errors.append(f"SEMANTIC_ERROR outputs.{name}.path: must not traverse a symlink")
        elif not target.exists():
            errors.append(f"SEMANTIC_ERROR outputs.{name}.path: file does not exist")
        elif target.is_symlink() or not target.is_file():
            errors.append(f"SEMANTIC_ERROR outputs.{name}.path: must be a regular non-symlink file")
        else:
            physical_target = target.resolve()
            if physical_target in physical_targets:
                errors.append(
                    f"SEMANTIC_ERROR outputs.{name}: duplicates physical target of "
                    f"outputs.{physical_targets[physical_target]}"
                )
            else:
                physical_targets[physical_target] = name
            try:
                actual_digest = hashlib.sha256(target.read_bytes()).hexdigest()
            except OSError as error:
                errors.append(f"SEMANTIC_ERROR outputs.{name}.path: unreadable file ({error.__class__.__name__})")
            else:
                if actual_digest != digest:
                    errors.append(f"SEMANTIC_ERROR outputs.{name}.sha256: does not match file")
        if root_kind == "durable-shared" and output.get("approval_ref"):
            approval = approvals.get(output["approval_ref"])
            expected = {"status": "approved", "sanitized": True, "output": name, "root": root_kind, "path": relative, "sha256": digest}
            if approval is None or any(approval[key] != value for key, value in expected.items()):
                errors.append(f"SEMANTIC_ERROR outputs.{name}.approval_ref: lacks an exact approved sanitized promotion tuple")

    scores = evaluation["scores"]
    score_contract_valid = False
    if set(scores) != set(SCORE_MAXIMA):
        errors.append("SEMANTIC_ERROR evaluation.scores: keys must match rubric")
    elif any(isinstance(scores[key], bool) or not isinstance(scores[key], (int, float)) or not 0 <= scores[key] <= maximum for key, maximum in SCORE_MAXIMA.items()):
        errors.append("SEMANTIC_ERROR evaluation.scores: values must be within rubric maxima")
    elif evaluation["total"] != sum(scores.values()):
        errors.append("SEMANTIC_ERROR evaluation.total: must equal weighted score sum")
    else:
        score_contract_valid = True
    if evaluation["hard_blockers"] and evaluation["decision"] == "accepted":
        errors.append("SEMANTIC_ERROR evaluation.decision: accepted cannot contain hard blockers")
    if evaluation["decision"] == "accepted":
        if score_contract_valid and (
            evaluation["total"] < 85 or any(scores[key] < 11 for key in CORE_SCORE_KEYS)
        ):
            errors.append("SEMANTIC_ERROR evaluation.decision: accepted requires threshold scores")
        if not timestamp(manifest["approval"]["approved_at"]) or not isinstance(manifest["approval"]["approved_by"], str) or not manifest["approval"]["approved_by"].strip():
            errors.append("SEMANTIC_ERROR approval: accepted requires approved_by and timezone timestamp")
    return sorted(errors)


def validate(root: Path, repository_root: Path | None = None) -> list[str]:
    documents: dict[str, Any] = {}
    errors: list[str] = []
    for name in FILES:
        path = root / name
        if not path.is_file():
            errors.append(f"DOCUMENT_ERROR {name}: missing")
            continue
        try:
            documents[name] = load(path)
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"DOCUMENT_ERROR {name}: invalid document ({error.__class__.__name__})")
    if errors:
        return sorted(errors)
    if any(isinstance(document, dict) and document.get("version") == 1 for document in documents.values()):
        return ["V1_MIGRATION_REQUIRED: migrate all package documents and manifest outputs to schema v2"]
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, ValueError, SchemaError) as error:
        return [f"VALIDATOR_ERROR schema: {error.__class__.__name__}"]
    structural = schema_errors(documents, schema)
    return structural if structural else semantic_errors(root, documents, repository_root)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path, help="Directory containing the seven UI specification files")
    parser.add_argument(
        "--repository-root",
        type=Path,
        help="Repository root used to resolve durable-shared outputs",
    )
    args = parser.parse_args()
    errors = validate(args.package, args.repository_root)
    if errors:
        print("\n".join(f"ERROR {error}" for error in errors))
        return 1
    print(f"OK {args.package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
