# Skill Live Canary Summary — 2026-07-23

## Basis

- Candidate repository: `/Users/daibin/Projects/repo-github/aicraft`
- Branch: `refact/skill-harness-refinement`
- Base HEAD: `b873705e9e7fe1de1b39f3cbf7489f00b03d3823`
- Host: Codex desktop on macOS.
- Fixtures: disposable repositories under `/private/tmp`; raw prompts and outputs are not published.

This is behavior evidence for the named scenarios only. It is not catalog-wide
certification and does not replace target-repository runtime validation.

## Results

| # | Skill path | Scenario | Result | Important gap or failure |
| --- | --- | --- | --- | --- |
| 1 | `repo-map` | non-Git container with two independent child Git roots | Pass | correctly kept a local unversioned map and marked runtime/API ownership not verified |
| 2 | `ui-spec` → `dev-frontend` | selected visual source to UI contract and standalone implementation | Partial | contract and static assertions passed; built-in Browser was unavailable, so rendering and pixel evidence remain `Not verified` |
| 3 | `dev-rust` | failing normalization tests to minimal Rust repair | Pass | red/green, format, check, test, and final diff passed; build artifacts remained untracked and were reported rather than deleted |
| 4 | `repo-review` | authorization-sensitive Worktree subprocess diff | Pass | ordinary fixed-basis review found the reachable regression without requiring a separate scanner or handoff |
| 5 | `repo-delivery` | exactly one local commit, no other Git operation | Pass | staged scope and final clean branch were proven; push, integration, PR, cleanup, and remote claims stayed outside authorization |
| 6 | `ask-chatgpt` | package-only decision challenge with no browser or send | Pass after refinement | first run silently added `/.codex/` to `.git/info/exclude`; the Skill now forbids tracked or local ignore changes without authorization, and a rerun against a pre-ignored path passed |

## Refinements From Failure Trajectories

1. `ask-chatgpt` now requires an already ignored approved package path and stops instead
   of changing tracked or local ignore configuration without authorization.
2. Browser availability is a host capability gate. The UI workflow must retain
   `Not verified`; it must not fall back to the user's external Chrome.
3. `repo-review` treats authentication, authorization, secrets, untrusted input, and
   related risks as part of the ordinary Standards axis. They do not trigger a
   separate scanner, workspace, or handoff.

## Static Validation

`bash scripts/check-skills.sh` used Homebrew Python through `uv`, confirmed shared
protocol copies, validated 14 packages, and passed 54 unit tests plus
`git diff --check`. Static validation proves package structure and repository contracts,
not browser behavior, external ChatGPT behavior, or complete security coverage.
