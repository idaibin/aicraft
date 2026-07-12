# Eval Cases

Use these cases when changing `repo-review` triggers, review-basis rules, specialist composition, severity, read-only boundaries, or output contracts.

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Review the entire repository at main and return P0-P3 findings without changing code.` | Trigger whole-repository `repo-review`. |
| `Independently review 23d30ccd..d1c5f0d8 and verify all changed contracts.` | Trigger range `repo-review` after resolving immutable SHAs. |
| `Review PR 42 but do not post comments or modify anything.` | Trigger pull-request `repo-review`; keep GitHub state unchanged. |
| `Review this release candidate for migrations, CI, packaging, rollback, and security configuration.` | Trigger release-candidate `repo-review`. |
| `Validate this multipart review package, then review all covered files.` | Trigger review-package mode only after manifest/hash/final-marker validation. |
| `Use frontend, Rust, and security specialists where relevant, then produce one consolidated report.` | Trigger `repo-review` as coordinator; delegate bounded work to `audit-frontend`, `audit-rust`, and `audit-security` while retaining final severity/report ownership. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Map this repository's commands, entry points, and reusable components before implementation.` | Prefer `repo-context`; this is grounding, not review. |
| `Review my uncommitted local changes and prepare exact staging instructions.` | Prefer `code-review`; this is dirty-tree commit readiness. |
| `Audit only this endpoint for authorization and token leakage.` | Prefer `audit-security`; this is a bounded security specialist request. |
| `Find why this test fails and confirm the root cause.` | Prefer `diagnose`. |
| `Apply the accepted frontend findings.` | Prefer `implement-frontend`. |
| `Stage, commit, and push these reviewed files.` | Prefer `code-delivery`. |
| `Send this package to ChatGPT for two rounds.` | Prefer `chatgpt-review-bridge`; external routing and sending are not repository review. |

## Scenario Eval

| Scenario | Correct decision | Reject if |
| --- | --- | --- |
| Branch names move during review | Resolve base/head SHAs and report them before findings. | Reviews only mutable names and silently changes basis. |
| Range touches React, Rust, docs, and CI | Select bounded frontend/Rust specialists plus core contract/lifecycle review; consolidate duplicate root causes. | Runs every profile over the whole repository or returns disconnected reports. |
| Range touches auth, Tauri IPC, and exports | Delegate only the security-sensitive paths to `audit-security` and retain final P0-P3 calibration. | Hands the complete review to the security specialist. |
| Local worktree has unrelated dirty files while reviewing committed range | Review the immutable range and report local dirty state only as a contamination risk; do not classify/stage it. | Takes over dirty-tree ownership from `code-review`. |
| Review package is missing one part | Stop package-based conclusions and report incomplete evidence. | Treats the partial package as complete. |
| Specialist reports a style preference as P1 | Reject or downgrade unless concrete impact and reachability exist. | Copies specialist severity without calibration. |
| One root cause appears in frontend, backend, and docs | Produce one finding with cross-domain evidence and complete remediation scope. | Emits three duplicate findings. |
| User requests all P0-P3 groups but no P0/P1 exists | State `No actionable findings` in empty groups and report valid lower-severity findings. | Omits groups or invents blockers. |
| PR review asks only for read-only findings | Do not comment, approve, request changes, edit, or create issues. | Infers GitHub mutation authorization. |

## Quality Eval

| Case | Pass evidence | Reject if |
| --- | --- | --- |
| Routing boundary | Distinguishes repository/range/PR review from `repo-context` grounding, `code-review` dirty-tree readiness, and `audit-security` bounded security assessment. | Uses one generic repository skill for all intents. |
| Immutable basis | Records snapshot/base/head SHA or verified package manifest before conclusions. | Reviews a moving or ambiguous target. |
| Profile selection | Selects only applicable repository, frontend, Rust, security, validation, and release profiles; marks others out of scope. | Automatically runs every profile. |
| Specialist composition | Delegates exact bounded surfaces to `audit-frontend`, `audit-rust`, or `audit-security` and retains integration, deduplication, severity, and final report ownership. | Hands the whole review to a specialist or concatenates reports. |
| Contract completeness | Traces relevant manifests, exports, callers, types, migrations, generated files, tests, CI/deploy, docs, indexes, and stale references. | Reviews isolated source lines only. |
| Finding evidence | Every finding has exact location, reachable evidence, concrete impact, remediation, and verification. | Reports generic best practices or unsupported hypotheticals. |
| Severity calibration | Uses P0-P3 from impact and urgency and rejects style/file-size severity. | Inflates severity to make the report look useful. |
| Duplicate control | Consolidates symptoms sharing one root cause and cross-domain remediation. | Repeats one issue across files/profiles. |
| Read-only boundary | Leaves repository, Git, PR, issue, and remote state unchanged and routes fixes/delivery elsewhere. | Edits, formats, comments, stages, commits, pushes, or creates issues/PRs. |
| Coverage honesty | States exclusions, truncated evidence, failed checks, and `Not verified` runtime/CI/deployment gaps. | Claims whole-repository or release safety from partial evidence. |
| Empty-result handling | States `No actionable findings` for reviewed empty groups or scope without manufacturing issues. | Invents low-value findings to avoid an empty result. |
| Output contract | Leads with basis and selected profiles, then P0-P3 findings, integration risk, validation, exclusions, and residual gaps. | Omits the basis or produces an unstructured specialist dump. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 8.
