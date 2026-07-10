---
name: code-context
description: "Use when the user explicitly asks to ground repository work, map real files, commands, entry points, project docs or classes, preview AGENTS/project-map content, inventory existing page/component or Rust interface reuse candidates, or compare docs and code before implementation."
---

# Code Context

## Overview

Establish repository context from real files, not assumptions. Use this when the
requested deliverable is onboarding, a targeted reuse/interface inventory, doc
bootstrap, or doc/code alignment. Generic implementation stays with
`implement-frontend`, `implement-rust`, or the repository's implementation
workflow, which performs its own targeted search when no current context report exists.

## Workflow

1. Read repo guidance first: root `AGENTS.md`, nearest subproject `AGENTS.md`, or `AGENT.md` fallback.
2. Run `git status --short` before drawing conclusions or planning writes.
3. Inspect only the manifests, configs, commands, entry points, and docs needed for the current request.
4. Identify the project class and any repository-defined toolchain, directory, naming, reuse, or structural lifecycle standard.
5. Before page, component, or Rust interface work, build a targeted inventory of analogous implementations. For frontend work include routes, pages, layouts, components, hooks, services, and shared UI. For Rust/API work include architecture docs, route registration, handlers, services, repositories, traits, types/DTOs, error mapping, migrations, callers, and tests. Identify reuse and reference candidates before proposing new files or interfaces.
6. For monorepos, inspect the workspace root first, then only relevant app/package boundaries; mark unrelated areas `Not verified`.
7. Choose the mode: Bootstrap or Alignment.
8. Stop once the requested context can be answered with evidence; do not crawl large trees by default.
9. Run only repo-defined checks when checks are needed and safe.

## Modes

- **Bootstrap:** preview missing `AGENTS.md`, `docs/project-map.md`, or equivalent docs from bundled templates; write only after explicit confirmation.
- **Alignment:** compare existing docs against manifests, configs, commands, entry points, project classification, current source layout, reuse/reference inventory, and structural lifecycle; report stale, missing, incorrect, or duplicated claims.

## Do Not Use For

- Existing local diff review, commit grouping, or staging plans; use `code-review`.
- Future implementation planning or subagent task splitting; use `code-planner`.
- Browser page operation or real desktop-client verification; use `ops-browser` or `ops-client`.
- Security-only review after the target surface is already known; use `code-security`.

## Hard Rules

- Keep context discovery and doc review read-only unless the user explicitly asks for writes.
- Use real paths, commands, configs, and code evidence; do not invent missing layers.
- Say `Not found` for missing files, layers, or commands.
- Say `Not verified` for unchecked areas or runtime claims.
- Treat local `prompts/` as optional; bundled references must be sufficient after publishing.
- Preview generated docs before writing unless implementation is explicitly requested.
- Preserve unrelated local changes.
- Do not impose one directory or toolchain template across different project classes. Treat documented legacy, prototype, multi-process, framework-native, and protected production layouts as explicit evidence.
- Do not recommend a new page, component, endpoint, handler, service, repository, trait, type/DTO, helper, hook, or shared layer before reading relevant docs and running a targeted existing-file and symbol search. Report the nearest reusable or reference implementation, or state `Not found` and justify the new path or interface.

## Output Contract

Start with verified current truth and project class, then report the targeted directory/file inventory, reuse and reference candidates, missing items, standards drift, doc/code mismatches, or proposed docs. Include commands run, new-file justification, validation status, structural lifecycle gaps, and anything `Not verified`.

## Skill Maintenance

When maintaining this package, update `references/eval-cases.md`, `references/usage.md`, and `agents/openai.yaml` with trigger, mode, or output changes. In AICraft, run `python3 scripts/validate-skills.py` before publishing; end-user installs use `npx skills add https://github.com/idaibin/aicraft`, and end-user updates use `npx skills update`.

## References

- See [references/usage.md](references/usage.md) for summary, triggers, and examples.
- See [references/checklist.md](references/checklist.md) for scan order and reporting details.
- See [references/prompt-templates.md](references/prompt-templates.md) for bundled bootstrap templates.
- See [references/eval-cases.md](references/eval-cases.md) for trigger and quality evals.
