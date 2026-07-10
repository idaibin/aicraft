# Eval Cases

Use these cases when changing `code-context` triggers, workflow, outputs, or metadata.

## Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `Understand this repository first, confirm real commands and entry points, and do not guess.` | Should trigger `code-context`. | Repository grounding. |
| `Do not guess the startup path; confirm the real commands and entry points first.` | Should trigger `code-context`. | Command and entry-point grounding. |
| `Check whether existing project docs match the code.` | Should trigger `code-context`. | Doc/code alignment. |
| `Classify these repositories and check whether same-class directory standards match the manifests.` | Should trigger `code-context`. | Project-class and structure alignment. |
| `Before building this page, list existing routes and components and find reusable or reference implementations.` | Should trigger `code-context`. | Reuse-first frontend grounding. |
| `Before adding this Rust API, map the existing docs, routes, handlers, services, repos, DTOs, errors, callers, and tests.` | Should trigger `code-context`. | Reuse-first Rust interface grounding. |

## Non-Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `Initialize a login feature and start implementing directly.` | Should not trigger `code-context`. | Generic implementation task. |
| `Review all local changes and split commits.` | Should prefer `code-review`. | Dirty-tree review. |
| `Split this migration into executable tasks.` | Should prefer `code-planner`. | Work planning. |
| `Verify this local web app in the browser and take a screenshot.` | Should prefer `ops-browser`. | Browser operation task. |
| `Review this API for authorization risk.` | Should prefer `code-security`. | Security review task. |

## Quality Eval

| Case | Expected evidence | Reject if |
| --- | --- | --- |
| Onboarding | Reads repo guidance, checks `git status --short`, maps real commands and paths, and stops when enough evidence exists. | Invents commands or crawls unrelated areas. |
| Large monorepo | Reads root workspace evidence and relevant package boundaries only; marks unrelated areas `Not verified`. | Inspects every package without task need. |
| Project-class alignment | Identifies real project classes, compares only equivalent layouts, and records protected or framework-native exceptions. | Forces one directory tree across Web/Rust, Tauri, CLI, service, and content projects. |
| Structural lifecycle | Checks manifests, exports, commands, tests, CI/deploy paths, architecture docs, project maps, and indexes when paths are added, reused, moved, or deleted. | Reviews source directories while ignoring ownership records and stale references. |
| Reuse inventory | Uses targeted file/symbol search, lists relevant existing pages/components/layouts/shared UI, and classifies candidates as reusable, reference-only, unrelated, or `Not found`. | Suggests new files from a guessed directory tree or scans the whole repository without task relevance. |
| New-file gate | Names the closest existing implementation and justifies why reuse or adaptation is insufficient before proposing a new page/component path. | Creates a parallel component or naming pattern without checking existing code. |
| Rust interface inventory | Traces docs, route/method/auth, handler, service, repository, trait/type/DTO, errors, persistence, callers, and tests; classifies reuse, extension, reference, unrelated, or `Not found`. | Suggests a new endpoint or trait after inspecting only one source file. |
| New-interface gate | Names the closest existing Rust contract and explains why reuse or extension is insufficient before proposing a new public API, endpoint, trait, or DTO family. | Creates a parallel interface or error model without checking docs and existing modules. |
| Bootstrap docs | Uses bundled templates, previews drafts, and writes only after confirmation. | Writes before preview approval. |
| Publish readiness | Keeps the package self-contained, updates eval cases and metadata, and validates with `python3 scripts/validate-skills.py`. | Requires repository-local prompts or skips source validation. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 7.
