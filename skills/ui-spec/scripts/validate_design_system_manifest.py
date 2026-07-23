#!/usr/bin/env python3
"""Validate a design-system automation manifest against repository files."""

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


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "assets" / "design-system-manifest.schema.json"


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


def timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        return datetime.fromisoformat(value.strip().replace("Z", "+00:00")).tzinfo is not None
    except ValueError:
        return False


def resolve_regular_file(repository_root: Path, relative: str) -> tuple[Path | None, str | None]:
    if not safe_relative(relative):
        return None, "must be a safe repository-relative POSIX path"
    candidate = repository_root / PurePosixPath(relative)
    try:
        candidate.resolve(strict=False).relative_to(repository_root.resolve(strict=False))
    except ValueError:
        return None, "escapes repository root"
    current = repository_root
    for part in PurePosixPath(relative).parts:
        current /= part
        if current.is_symlink():
            return None, "must not traverse a symlink"
    if not candidate.exists():
        return None, "file does not exist"
    if not candidate.is_file():
        return None, "must be a regular file"
    return candidate, None


def schema_errors(document: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(
        validator.iter_errors(document),
        key=lambda item: (tuple(map(str, item.absolute_path)), item.message),
    ):
        location = ".".join(str(part) for part in error.absolute_path) or "manifest"
        errors.append(f"SCHEMA_ERROR {location}: {error.message}")
    return errors


def validate(manifest_path: Path, repository_root: Path) -> list[str]:
    if manifest_path.is_symlink() or not manifest_path.is_file():
        return ["DOCUMENT_ERROR manifest: must be a regular non-symlink file"]
    if not repository_root.is_dir():
        return ["DOCUMENT_ERROR repository_root: must be an existing directory"]
    try:
        document = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"DOCUMENT_ERROR manifest: invalid document ({error.__class__.__name__})"]
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, ValueError, SchemaError) as error:
        return [f"VALIDATOR_ERROR schema: {error.__class__.__name__}"]
    structural = schema_errors(document, schema)
    if structural:
        return structural

    errors: list[str] = []
    if not timestamp(document["approval"]["approved_at"]):
        errors.append("SEMANTIC_ERROR approval.approved_at: requires a timezone-aware timestamp")

    consumer = document["consumer"]
    consumer_file, consumer_error = resolve_regular_file(repository_root, consumer["path"])
    if consumer_error:
        errors.append(f"SEMANTIC_ERROR consumer.path: {consumer_error}")
    elif hashlib.sha256(consumer_file.read_bytes()).hexdigest() != consumer["sha256"]:
        errors.append("CONSUMER_CONFLICT consumer.sha256: automation consumer has changed")

    authority = document["semantic_authority"]
    authority_file, authority_error = resolve_regular_file(repository_root, authority["path"])
    if authority_error:
        errors.append(f"SEMANTIC_ERROR semantic_authority.path: {authority_error}")
    elif hashlib.sha256(authority_file.read_bytes()).hexdigest() != authority["sha256"]:
        errors.append("AUTHORITY_CONFLICT semantic_authority.sha256: semantic authority has changed")

    ids: set[str] = set()
    paths: set[str] = {consumer["path"], authority["path"]}
    if consumer["path"] == authority["path"]:
        errors.append("SEMANTIC_ERROR semantic_authority.path: duplicates consumer path")
    for index, binding in enumerate(document["bindings"]):
        if binding["id"] in ids:
            errors.append(f"SEMANTIC_ERROR bindings.{index}.id: duplicate binding id")
        ids.add(binding["id"])
        if binding["path"] in paths:
            errors.append(f"SEMANTIC_ERROR bindings.{index}.path: duplicate consumer, authority, or binding path")
        paths.add(binding["path"])
        target, target_error = resolve_regular_file(repository_root, binding["path"])
        if target_error:
            errors.append(f"SEMANTIC_ERROR bindings.{index}.path: {target_error}")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != binding["sha256"]:
            errors.append(f"BINDING_CONFLICT bindings.{index}.sha256: bound asset has changed")
    return sorted(errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--repository-root", required=True, type=Path)
    args = parser.parse_args()
    errors = validate(args.manifest, args.repository_root)
    if errors:
        print("\n".join(f"ERROR {error}" for error in errors))
        return 1
    print(f"OK {args.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
