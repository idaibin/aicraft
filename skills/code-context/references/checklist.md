# Code Context Checklist

Use this checklist when applying `code-context` to understand a repository, bootstrap missing context docs, or review existing docs against code. Trigger phrases include `repository context`, `understand this project`, `do not guess`, `real commands`, `real entry points`, and `doc/code alignment`.

## Scan Order

1. Read `AGENTS.md` first when present; use nearest subproject `AGENTS.md` and `AGENT.md` only as fallback.
2. Run `git status --short` to capture real dirty-tree state.
3. Read `README.md`, root manifests, lockfiles, and framework/build configs.
4. Classify the project from evidence: web app, Web/Rust service, Rust library/CLI, Tauri/native client, compact service, content site, multi-process system, or a repository-defined equivalent.
5. Read repository standards for toolchain, package manager, directory, naming, reuse, and add/move/delete lifecycle when present.
6. For page/component tasks, use a targeted file and symbol search to inventory existing routes, pages, layouts, components, hooks, services, shared UI, tests, and analogous implementations.
7. For Rust/API tasks, inventory relevant architecture/API docs, route registration, handlers, services, repositories, traits/impls, types/DTOs, error types and response mapping, migrations, callers/consumers, tests, examples, and analogous feature modules.
8. Classify each relevant candidate as directly reusable, extensible, reference-only, unrelated, or `Not found` before proposing a new file or interface.
9. If the repo is a monorepo, identify the workspace root and then inspect only the app/package boundaries relevant to the request.
10. Map the real source tree only to the depth needed for the current answer.
11. Read the files that implement project-specific conventions when those conventions affect the requested context.
12. Run baseline checks only with commands already defined by the repo.
13. Detect context doc state:
   - missing or sparse docs: use Bootstrap mode
   - existing docs with current-truth claims: use Alignment mode

## What To Report

- Tech stack
- Package manager
- Runtime requirements
- Startup, dev, serve, preview, build, lint, typecheck, and test commands
- Real paths for entry points, routes, shared components, application layers or services, state, styles, and tests
- Project class, reference layout, current exceptions, and protected runtime/deployment boundaries
- Structural lifecycle rules for adding, reusing, moving, renaming, or deleting owned code
- Existing page/component/layout/shared-UI inventory relevant to the task
- Existing Rust/API interface chain relevant to the task: docs, route, handler, service, repository, trait/type, errors, persistence, caller, and tests
- Direct reuse candidates, nearest reference implementations, naming/placement patterns, and the reason any new file is necessary
- Files that are absent, reported as `Not found`
- Dirty worktree state and unrelated changes that must be preserved
- Checks performed, failures, and `Not verified` items
- Selected bundled templates, optional local prompt assets, and previewed drafts in Bootstrap mode
- Doc/code mismatches and suggested changes in Alignment mode

## Baseline Check Rules

- Prefer existing scripts or documented commands.
- Do not invent replacement commands.
- If a command is missing, report `Not found`.
- If a command fails, classify it as:
  - environment issue
  - configuration issue
  - existing project issue
- If a repo or user requires a specific tool, browser, command, or runtime, do not substitute another one. Report unavailable requirements as blockers.

## Bootstrap Mode

- Use when `AGENTS.md`, `docs/project-map.md`, or equivalent context docs are missing.
- Use `references/prompt-templates.md` first. It is bundled with the skill and must work after publishing.
- If local `prompts/` exists, inspect it only as an optional override or project-specific supplement.
- Prefer initialization, repo-rule, task-start, and doc-alignment templates.
- Explain which bundled templates or local prompt assets were selected and why.
- Generate draft docs from repository truth, not from template or prompt assumptions.
- Preview drafts first. Do not write files until the user confirms.

## Alignment Mode

- Use when project docs already exist.
- Compare docs against manifests, configs, commands, source entry points, routes/modules, tests, and workspace membership.
- Compare project classification and directory claims against the real app, crate, package, process, and framework boundaries.
- Check whether add/reuse/move/delete rules cover manifests, exports, commands, tests, CI/deploy paths, architecture/project-map docs, and indexes.
- Check whether docs identify the actual reusable page/component/layout surfaces and whether duplicate implementations or competing naming/placement patterns have appeared.
- Check whether Rust/API docs match the current route, method, auth/permission, request/response types, serialization, error mapping, persistence, callers, tests, and module placement.
- Check whether a proposed new interface can extend an existing trait, handler/service/repository pattern, DTO family, error type, or feature module before creating a parallel contract.
- Treat different project classes as separate standards; do not recommend a mechanical directory rewrite without an explicit migration requirement.
- Report stale, missing, incorrect, duplicated, or unverifiable doc claims.
- Suggest exact doc changes or sections to update.
- Do not modify docs unless the user explicitly asks.

## Read-Only Rules

- Do not modify source files during context discovery or doc review.
- Do not generate file writes unless the user explicitly confirms a preview or asks for writing.
- If docs are drafted, keep current truth separate from history or plans.
- Preserve unrelated local changes.

## Draft Output Outline

### AGENTS.md
- Repository purpose
- Directory structure
- Working rules
- Code change constraints
- Required checks after changes
- Final report format
- Disallowed actions

### docs/project-map.md
- Tech stack
- Install / start / test / build commands
- Directory structure
- File chain for typical page work
- Locations for components, interfaces, state, styles, and tests
- Frequent edit areas
- Risky areas
- Recommended reading order
