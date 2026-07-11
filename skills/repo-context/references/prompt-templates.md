# Prompt Templates

These templates are bundled with `repo-context` so the skill remains usable after publishing. Local `prompts/` files may supplement these templates, but they are never required.

## Template Selection

- Missing `AGENTS.md`: use the AGENTS.md bootstrap template.
- Missing `docs/project-map.md`: use the project map bootstrap template.
- Existing docs present: use the doc/code alignment review template.
- New task before edits: use the task-start context template.

Templates provide structure only. Repository files, configs, commands, and code are the source of truth.

## AGENTS.md Bootstrap Template

Use after reading real repo files. Preview the draft first.

Required sections:

- Repository purpose
- Directory structure
- Working rules
- Code change constraints
- Required checks after changes
- Final report format
- Disallowed actions

Hard requirements:

- Use real paths and real command names.
- Write `Not found` for missing layers or commands.
- Keep rules specific to the repository.
- Do not include generic best-practice filler.
- Do not write the file until the user approves the preview.

## Project Map Bootstrap Template

Use for `docs/project-map.md` or an equivalent context map.

Required sections:

- Tech stack
- Install, start, test, lint, typecheck, and build commands
- Runtime and package manager requirements
- Directory structure
- Typical file chain for page, API, backend, CLI, or worker changes
- Components, services, state, styles, tests, and config locations
- Existing reusable pages, layouts, components, hooks, services, and shared UI relevant to common tasks
- Existing Rust/API routes, handlers, services, repositories, traits/types, DTOs, errors, migrations, callers, and tests relevant to common tasks
- Reference implementations, naming/placement patterns, and new-file decision rule
- Frequent edit areas
- High-risk areas
- Recommended reading order for new tasks

Hard requirements:

- Use grouped path tables when that is clearer than prose.
- Separate current truth from historical docs or plans.
- Mark unchecked items as `Not verified`.
- Do not invent commands.

## Doc/Code Alignment Review Template

Use when context docs already exist.

Review against:

- manifests and lockfiles
- command sources such as `package.json`, `justfile`, `Makefile`, or CI configs
- workspace membership and package boundaries
- source entry points, routes, modules, services, and tests
- current repo guidance files
- repository-defined project class, directory, naming, reuse, and structural lifecycle rules

Classify findings:

- stale: old paths, commands, package managers, or architecture
- missing: important current commands, paths, constraints, or risks are absent
- incorrect: docs contradict code or config
- duplicated: command truth is repeated in multiple docs and likely to drift
- structural drift: manifests, exports, commands, tests, CI/deploy paths, architecture docs, or indexes disagree after add/reuse/move/delete work
- unverifiable: claim could not be checked from current repo evidence

Output:

- findings first, ordered by impact
- exact doc file or section when possible
- suggested replacement wording when useful
- validation performed and remaining `Not verified` items

## Task-Start Context Template

Use when the user is about to start implementation in a repo.

Required first pass:

- read relevant `AGENTS.md`
- inspect related docs and code
- run `git status --short`
- identify allowed and disallowed edit scope
- identify existing commands needed for verification
- inventory relevant existing implementations before proposing a new page, component, endpoint, handler, service, repository, trait, type/DTO, hook, or helper

Output:

- current context in one short paragraph
- proposed edit boundary
- direct reuse candidate, nearest reference implementation, or `Not found` with new-file justification
- verification commands to run after changes
- risks or blockers before editing
