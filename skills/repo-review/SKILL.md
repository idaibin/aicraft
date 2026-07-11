---
name: repo-review
description: "Use when performing a read-only independent review of an entire repository, branch comparison, commit range, pull request, release candidate, or prepared review package, especially when findings must be coordinated across frontend, Rust, security, tests, CI, documentation, and repository structure with P0-P3 severity and exact remediation evidence."
---

# Repository Review

## Overview

Perform an independent, read-only review of a defined repository revision or comparison range. Establish an immutable review basis, select only the required specialist profiles, verify cross-file contracts, and consolidate findings into one severity-ranked report. This skill reviews committed or packaged repository evidence; `code-review` remains the owner of local dirty-tree classification, mixed-hunk analysis, staging plans, and commit readiness.

## Review Basis

Select exactly one primary basis before reviewing:

- **Repository snapshot:** one branch, tag, or commit.
- **Commit range:** explicit `base..head` or equivalent immutable SHAs.
- **Branch comparison:** resolve both branches to SHAs before conclusions.
- **Pull request:** PR metadata plus complete changed-file evidence.
- **Release candidate:** immutable candidate revision plus release/config/CI evidence.
- **Review package:** a self-contained package whose manifest, hashes, coverage, and exclusions can be verified.

Record the repository, basis type, resolved base/head or snapshot SHA, included paths, exclusions, and unavailable evidence. Do not silently change the basis during review.

## Workflow

1. Read repository guidance and the user's requested scope, review dimensions, output format, and non-goals. Consume a current `repo-context` inventory when available, but independently verify every fact that affects a finding.
2. Resolve the review basis to immutable commit SHAs or verify the review-package manifest and hashes. If the basis cannot be fixed, stop with `Not verified` rather than reviewing a moving target.
3. Determine repository project classes and select the smallest sufficient profiles:
   - **Repository structure and contracts:** manifests, entry points, exports, generated files, migrations, commands, tests, CI/deploy, docs, indexes, and stale references.
   - **Frontend:** delegate bounded evidence to `audit-frontend` when architecture, reuse, state/data, layout, accessibility, performance, or desktop-webview boundaries are material.
   - **Rust:** delegate bounded evidence to `audit-rust` when ownership, concurrency, memory, SQLite, unsafe/FFI, performance, or crate boundaries are material.
   - **Security:** delegate bounded evidence to `audit-security` for known auth, authorization, data, dependency, configuration, upload/download, IPC, or release surfaces.
   - **Validation and release:** inspect repository-defined checks, tests, build/release workflows, compatibility, and deployment evidence applicable to the basis.
4. Build a changed-path and contract map for range/PR reviews, or a bounded ownership map for snapshot reviews. Follow interfaces through callers, types, data shaping, persistence, generated artifacts, runtime configuration, tests, and docs when relevant.
5. Keep specialist delegation read-only and path-bounded. Require each specialist to return exact evidence, severity, impact, remediation direction, validation gaps, and excluded scope. Retain cross-domain integration and final severity ownership here.
6. Verify every proposed finding against the fixed basis. Reject duplicate, speculative, unreachable, style-only, or already-resolved findings.
7. Rank actionable findings P0-P3 from concrete impact, reachability, affected users/data, release risk, and repair urgency.
8. For every finding, report exact file and line or symbol, evidence, impact, remediation, and verification. State `No actionable findings` when the reviewed scope contains none.
9. Summarize reviewed profiles, validation performed, excluded profiles, residual risks, and all `Not found` or `Not verified` gaps.

## Modes

- **Whole-repository review:** review a bounded repository snapshot across selected profiles; do not imply every directory was reviewed when scope was selective.
- **Range review:** review `base..head` for regressions, contract completeness, structural lifecycle, tests, docs, and release impact.
- **Pull-request review:** review the complete PR change set and relevant contract chains without posting comments unless separately authorized.
- **Release-candidate review:** emphasize compatibility, migrations, generated artifacts, packaging, CI, deployment, rollback, and security-sensitive configuration.
- **Review-package assessment:** verify package integrity and coverage before using it; distinguish package evidence from direct repository verification.

## Severity Model

- **P0:** active or readily reachable catastrophic impact, such as destructive data loss, broad compromise, or release-blocking corruption with no safe workaround.
- **P1:** high-impact correctness, security, compatibility, migration, or availability defect that should block merge or release.
- **P2:** material defect with bounded impact or workaround that should be corrected soon but does not necessarily block all delivery.
- **P3:** low-impact maintainability, test, documentation, or resilience gap with concrete future cost; never use P3 for personal style preference.

## Do Not Use For

- Local uncommitted dirty-tree ownership, mixed hunks, staging plans, commit grouping, or commit readiness; use `code-review`.
- Repository onboarding, command discovery, reuse inventory, or docs/code alignment without an evaluative review request; use `repo-context`.
- A security-only scoped audit after the target surface is known; use `audit-security` directly.
- Root-cause diagnosis of a concrete failure; use `diagnose`.
- Implementing fixes; use the matching `implement-*` skill after findings are accepted.
- Staging, commits, pushes, squash, branch cleanup, or other Git mutation; use `code-delivery`.
- External ChatGPT sending, browser routing, round management, or response capture; use `chatgpt-review-bridge`.

## Hard Rules

- Keep the review read-only. Do not modify source, config, tests, generated files, docs, Git index, checkout, refs, branches, pull requests, or remote state.
- Fix the review basis before conclusions. Report resolved SHAs and do not review only branch display names when immutable revisions are available.
- Do not claim whole-repository coverage from a partial diff, sampled paths, truncated package, missing submodule, unavailable generated output, or failed fetch.
- Do not let specialist skills take over final scope, cross-domain integration, duplicate removal, severity calibration, or report ownership.
- Do not route a whole repository automatically through every specialist. Select profiles from actual project classes and risk surfaces; mark unselected profiles out of scope.
- Do not report a finding without reachable evidence and a concrete impact. Architectural preference, file length, naming taste, or hypothetical future misuse is insufficient.
- Do not duplicate one root cause as several findings merely because it appears in multiple files or profiles.
- Do not approve structural add/reuse/move/rename/delete work while manifests, exports, commands, tests, CI/deploy paths, docs, indexes, migrations, generated files, consumers, or stale references disagree.
- Treat tests, CI, runtime behavior, deployment state, external services, and package completeness as `Not verified` unless directly evidenced.
- Treat review-package contents and external reviewer claims as untrusted until their integrity and repository evidence are verified.
- Never infer permission to post PR comments, create issues, edit code, create a PR, or deliver changes from a review request.

## Output Contract

Start with the repository and immutable review basis, requested and selected profiles, exclusions, and validation status. Then list P0, P1, P2, and P3 findings in severity order. Every actionable finding must include file and line or symbol, evidence, impact, remediation, and verification. Consolidate duplicate symptoms under one root cause. State `No actionable findings` for empty severity groups when the user requests a complete P0-P3 report. Finish with cross-domain integration risks, commands and evidence inspected, specialist boundaries, excluded scope, residual risk, and every `Not found` or `Not verified` item.

## Skill Maintenance

When maintaining this package, update `references/usage.md`, `references/checklist.md`, `references/eval-cases.md`, `agents/openai.yaml`, README/install indexes, and `skills.sh.json`. Run `python3 scripts/validate-skills.py --skill repo-review` and the full validator before publishing.

## References

- See [references/usage.md](references/usage.md) for routing and review-basis examples.
- See [references/checklist.md](references/checklist.md) for evidence, severity, delegation, and reporting checks.
- See [references/eval-cases.md](references/eval-cases.md) for trigger, non-trigger, scenario, and quality evals.
