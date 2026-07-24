#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! command -v npx >/dev/null 2>&1; then
  echo "required tool npx is missing" >&2
  exit 2
fi

design_md_path="skills/ui-spec/assets/DESIGN.md"
if [[ ! -f "$design_md_path" ]]; then
  echo "missing required DESIGN.md asset: $design_md_path" >&2
  exit 2
fi

export npm_config_cache="${npm_config_cache:-${TMPDIR:-/tmp}/aicraft-design-md-npm-cache}"
export npm_config_registry="${npm_config_registry:-https://registry.npmjs.org/}"
design_md_cli=(npx --yes -p @google/design.md@0.3.0 designmd)

tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/aicraft-design-md-XXXXXX")"
trap 'rm -rf -- "$tmp_dir"' EXIT

run_designmd_lint() {
  local target="$1"
  local output
  set +e
  output="$("${design_md_cli[@]}" lint --format json "$target" 2>&1)"
  local status=$?
  set -e
  printf '%s\n' "$output"
  return $status
}

extract_warning_count() {
  local output="$1"
  node -e '
const raw = process.argv[2];
const start = raw.indexOf("{");
if (start < 0) {
  process.exit(2);
}

const data = JSON.parse(raw.slice(start));
const summary = data.summary || {};
let warnings = summary.warnings;

if (typeof warnings !== "number") {
  const walk = (node) => {
    if (!node) return 0;
    if (Array.isArray(node)) {
      return node.reduce((acc, item) => acc + walk(item), 0);
    }
    if (typeof node === "object") {
      if (node.severity === "warning") {
        return 1;
      }
      return Object.values(node).reduce((acc, item) => acc + walk(item), 0);
    }
    return 0;
  };
  warnings = walk(data);
}

console.log(String(warnings));
' _ "$output"
}

guard_duplicate_h2() {
  local file="$1"
  local duplicates
  duplicates="$(node - "$file" <<'NODE'
const fs = require("fs");

const path = process.argv[2];
const lines = fs.readFileSync(path, "utf8").split(/\r?\n/);
const seen = new Map();
const reported = new Set();
const duplicates = [];

for (const line of lines) {
  const match = line.match(/^\s{0,3}##(?:(?:\s|$)(.*))$/);
  if (!match) {
    continue;
  }
  let heading = (match[1] || "").trim();
  heading = heading.replace(/\s+#{1,}\s*$/, "").trim();
  if (heading.length === 0) {
    continue;
  }
  const count = seen.get(heading) || 0;
  seen.set(heading, count + 1);
  if (count > 0 && !reported.has(heading)) {
    duplicates.push(heading);
    reported.add(heading);
  }
}

console.log(duplicates.join("\n"));
NODE
)"

  if [[ -n "$duplicates" ]]; then
    echo "duplicate H2 guard rejection in $(basename "$file"):" >&2
    echo "$duplicates" >&2
    return 1
  fi
  return 0
}

baseline_output="$(run_designmd_lint "$design_md_path")"
baseline_status=$?
if [[ $baseline_status -ne 0 ]]; then
  echo "baseline DESIGN.md lint failed" >&2
  exit 1
fi
if ! guard_duplicate_h2 "$design_md_path"; then
  echo "baseline DESIGN.md should not have duplicate H2 headings" >&2
  exit 1
fi
if [[ "$(extract_warning_count "$baseline_output")" -ne 0 ]]; then
  echo "$baseline_output" >&2
  echo "expected baseline DESIGN.md to have zero warnings" >&2
  exit 1
fi

tmp_unknown_h2="$tmp_dir/design_unknown.md"
cp "$design_md_path" "$tmp_unknown_h2"
printf '\n## Unknown H2 Section\n' >> "$tmp_unknown_h2"
if ! guard_duplicate_h2 "$tmp_unknown_h2"; then
  echo "unknown H2 variant should not trigger duplicate H2 guard" >&2
  exit 1
fi
unknown_output="$(run_designmd_lint "$tmp_unknown_h2")"
unknown_status=$?
if [[ $unknown_status -ne 0 ]]; then
  echo "$unknown_output" >&2
  echo "baseline DESIGN.md + unknown H2 lint failed" >&2
  exit 1
fi
if [[ "$(extract_warning_count "$unknown_output")" -ne 0 ]]; then
  echo "$unknown_output" >&2
  echo "expected no warnings after adding an unknown H2 section" >&2
  exit 1
fi

duplicate_h2_variants=(
  "## Overview"
  "  ## Overview"
  "## Overview ##"
)
blocked_duplicate_count=0

for duplicate_heading in "${duplicate_h2_variants[@]}"; do
  duplicate_variant_file="$tmp_dir/design_duplicate_overview_$(echo "${duplicate_heading// /_}" | tr -cd '[:alnum:]_').md"
  cp "$design_md_path" "$duplicate_variant_file"
  printf '\n%s\n' "$duplicate_heading" >> "$duplicate_variant_file"

  duplicate_output="$(run_designmd_lint "$duplicate_variant_file")"
  duplicate_status=$?
  if [[ $duplicate_status -ne 0 ]]; then
    echo "$duplicate_output" >&2
    echo "duplicate synthetic H2 lint failed for: $duplicate_heading" >&2
    exit 1
  fi
  if [[ "$(extract_warning_count "$duplicate_output")" -lt 1 ]]; then
    echo "$duplicate_output" >&2
    echo "duplicate synthetic H2 did not produce warning findings for: $duplicate_heading" >&2
    exit 1
  fi

  if ! guard_duplicate_h2 "$duplicate_variant_file"; then
    blocked_duplicate_count=$((blocked_duplicate_count + 1))
    continue
  fi

  echo "synthetic duplicate H2 was not blocked for: $duplicate_heading" >&2
  exit 1
done

if [[ $blocked_duplicate_count -ne "${#duplicate_h2_variants[@]}" ]]; then
  echo "some synthetic duplicate H2 variants did not trigger duplicate H2 guard" >&2
  exit 1
fi

echo "synthetic duplicate H2 variants were rejected by hard-blocking duplicate H2 guard" >&2

diff_output="$("${design_md_cli[@]}" diff "$design_md_path" "$design_md_path" --format json 2>&1)"
if ! echo "$diff_output" | grep -qE '\"regression\"[[:space:]]*:[[:space:]]*false'; then
  echo "designmd diff did not report regression false for identical files" >&2
  echo "$diff_output" >&2
  exit 1
fi

echo "design md contract regression checks passed"
