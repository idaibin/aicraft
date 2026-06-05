# Review Checklist

Use this checklist before planning or making commits in a dirty worktree, or when upgrading this skill from a trusted upstream source. Chinese trigger phrases include `提交前审查`, `审查所有改动`, `分类提交`, `拆分 commit`, `生成 commit message`, and `commit-reviewer 升级`.

## Required Evidence

- Read `AGENTS.md` first when present; use nearest `AGENTS.md` for subprojects and `AGENT.md` only as a fallback.
- Run `git status --short`.
- Run `git diff --stat` and `git diff --name-status`.
- If anything is staged, run `git diff --cached --stat` and `git diff --cached --name-status`.
- Inspect actual diffs for every file that may enter a commit group.
- Identify the complete local change scope before choosing the commit-planning or staging scope.
- If a remote source or version is supplied for this skill, use Upgrade mode.

## Inventory

- List files by state: modified, new, deleted, renamed, generated.
- Group files by intent, not by path alone.
- Separate code, docs, config, CI, deploy, and refactor work unless they are tightly coupled.
- Mark unrelated local changes explicitly and leave them untouched.

## Completeness

- Verify the functional change is closed.
- Verify changed files sit in the expected project directories and follow existing module/component boundaries.
- Verify changed code follows local naming, style, and implementation conventions.
- Verify docs were updated when contracts, commands, or paths changed.
- Verify docs and code do not contradict each other.
- Verify tests or validation commands were updated when behavior changed.
- Check type, lint, build, formatter, unused import, unused definition, and broken reference risk.
- Check for missing config, workflow, or path updates.
- Check for files that should not be committed.
- Record what was verified and what is still `Not verified`.

## Split Rules

- Prefer one semantic change per commit.
- Keep dependent files together when one file cannot stand alone.
- Keep code + migration together.
- Keep code + contract docs together when the docs describe the same change.
- Separate build/deploy/CI changes from feature behavior when possible.
- Separate docs-only changes from code changes when possible.
- Keep generated artifacts out unless they are the requested deliverable.

## Common Cases

- Feature work with tests and contract docs: one commit if the files describe the same change.
- Artifact or path renames across `justfile`, Dockerfiles, and workflows: one deploy commit.
- Repository docs and readmes that only describe the new contract: one docs commit.
- Generated outputs such as build caches or release artifacts: do not commit unless the artifact itself is the deliverable.
- User-owned local edits mixed with task files: stage only the requested slice and mention the excluded files.

## Do Not Commit

- Build outputs such as `target/`.
- Runtime logs, caches, screenshots, and temp files.
- Local env files and other machine-specific artifacts.
- Generated artifacts unless they are the intended deliverable.
- Unrelated local changes, even when they are already in the same directory.

## Staging Rules

- Prefer exact path-limited staging commands.
- Verify staged files before each commit.
- Do not use `git add .`, `git add -A`, or broad wildcard staging unless the user explicitly asks for that exact scope.
- If there are pre-existing staged files outside the current group, stop and report the conflict before committing.
- For direct user requests, default to the full reviewed local change scope unless the user explicitly limits the commit scope.
- If the user asks to commit only current context, current session, or this task's changes, default to staging only that subset after full-scope review.
- If another AI agent invokes this skill as a sub-workflow, follow that caller's stated scope after full-scope review.
- Ask before staging only when the requested subset is ambiguous, required files outside the subset appear necessary, or pre-existing staged files conflict with the requested scope.

## Commit Message Style

- Use Conventional Commits.
- Keep the message concise.
- Match the user's requested language or repository convention; otherwise use concise English.

## Upgrade Mode

- Use when the user supplies a GitHub URL, branch, tag, commit, directory, or file URL for updating this skill.
- Read `references/upstream-sources.md` for known default sources.
- Prefer commit SHA over moving branches; resolve and report the SHA when using a branch.
- Inspect upstream content read-only.
- Compare upstream `skills/commit-reviewer/` against local files.
- Classify candidates as skill-core, bundled-reference, agent-interface, or reject.
- Preview proposed changes first. Do not write files until the user confirms or explicitly asks for implementation.
- Keep the skill self-contained; do not introduce required external prompt dependencies.
- After writing, run stale-name, self-contained-reference, Markdown whitespace, YAML, `git diff --check`, and status checks.
