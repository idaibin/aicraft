# Repository Context

## Summary

Ground an agent in a repository before it guesses. Use it to map real commands, paths, docs, project conventions, ownership, and reuse candidates, or to preview context docs safely.

## Best For

- First-pass repository onboarding
- Real command and entry-point discovery
- `AGENTS.md` or project-map draft previews
- Doc/code alignment checks
- Project-class, directory-standard, and structural lifecycle alignment
- Existing page/component inventory and reuse/reference discovery before implementation
- Existing Rust/API interface-chain inventory before adding endpoints, traits, types, or modules

## Triggers

Use for prompts like:

- `Understand this project first; do not guess.`
- `Initialize repository context.`
- `Confirm the real directories, commands, and entry points.`
- `Confirm real commands and real entry points before choosing a launch path.`
- `Check whether project docs match the code.`
- `Classify these projects and check whether same-class directories and commands follow one standard.`
- `Check whether adding, reusing, moving, or deleting modules updates manifests and docs.`
- `List the existing pages and components relevant to this screen before creating anything.`
- `Find a reusable or reference implementation and explain whether a new component is necessary.`
- `Before adding this Rust endpoint, trace the existing docs, route, handler, service, repo, types, errors, callers, and tests.`
- `Find whether an existing trait or interface can be extended before creating another one.`
- `Draft AGENTS.md first; preview before writing.`

Do not use for generic feature initialization, dirty-tree commit review, immutable repository/range/PR review, scoped security audit, or implementation planning; prefer `code-review`, `repo-review`, `audit-security`, or `code-planner` for those.

## Output

Expect verified current truth, project class, targeted directory/file inventory, direct reuse candidates, nearest reference implementations, new-file justification, real paths and commands, standards drift, structural lifecycle gaps, missing items as `Not found`, unchecked areas as `Not verified`, and previews before any write.

## Maintenance

Use `references/eval-cases.md` for trigger and quality checks. In AICraft, validate with `python3 scripts/validate-skills.py --skill repo-context`; end-user installs use `npx skills add https://github.com/idaibin/aicraft`, and end-user updates use `npx skills update`.
