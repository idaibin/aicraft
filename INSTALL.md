# Install Skills

Use the standard `skills` CLI. The public source is `idaibin/skills`.

## Discover

```bash
npx skills@latest add idaibin/skills --list
```

The result must contain exactly these public packages:

```text
repo-map
domain-modeling
repo-review
repo-delivery
design-system
implement-frontend
implement-rust
audit-frontend
audit-rust
audit-security
ops-browser
ops-client
chatgpt-review
human-writing
```

The publishable source directories are:

- `skills/repo-map`
- `skills/domain-modeling`
- `skills/repo-review`
- `skills/repo-delivery`
- `skills/design-system`
- `skills/implement-frontend`
- `skills/implement-rust`
- `skills/audit-frontend`
- `skills/audit-rust`
- `skills/audit-security`
- `skills/ops-browser`
- `skills/ops-client`
- `skills/chatgpt-review`
- `skills/human-writing`

## Install

Choose Skills and agents interactively:

```bash
npx skills@latest add idaibin/skills
```

Install selected Skills into the current project for Codex:

```bash
npx skills@latest add idaibin/skills \
  --skill repo-map repo-review \
  --agent codex
```

Install selected Skills globally for Codex and Claude Code:

```bash
npx skills@latest add idaibin/skills \
  --skill repo-map domain-modeling repo-review repo-delivery \
  --global --agent codex claude-code
```

Install one Skill globally:

```bash
npx skills@latest add idaibin/skills \
  --skill audit-rust \
  --global --agent codex
```

Install all published Skills non-interactively only when that broad scope is
intentional:

```bash
npx skills@latest add idaibin/skills \
  --skill '*' --global --agent codex --yes
```

## Suggested Sets

Core read-only repository work:

```bash
npx skills@latest add idaibin/skills \
  --skill repo-map domain-modeling repo-review
```

Frontend design and implementation:

```bash
npx skills@latest add idaibin/skills \
  --skill design-system implement-frontend audit-frontend ops-browser repo-review
```

Rust implementation and audit:

```bash
npx skills@latest add idaibin/skills \
  --skill implement-rust audit-rust repo-review
```

These are documentation shortcuts, not custom CLI bundles or quality claims.

## Use Without Installing

```bash
npx skills@latest use idaibin/skills@audit-rust
```

## Inspect, Update, and Remove

```bash
npx skills list
npx skills list --global
npx skills update --project
npx skills update --global
npx skills remove audit-rust --global --agent codex
```

Updates depend on source metadata recorded by `skills add`. Manually copied
folders, inaccessible sources, and renamed packages may require removal and a
fresh installation. Restart long-running agent applications after an update so
they reload discovery metadata.

## Rename Migration

### Repository source

The public source changed from `idaibin/aicraft` to `idaibin/skills`. GitHub may
redirect the old repository URL, but installed source metadata should be moved
explicitly by removing the old tracked installation and adding the new source.

### Design Skill

`design-ui` was replaced by `design-system` to reflect creation, extraction,
maintenance, task design, and evaluation of a repository-owned design system.
The new Skill still routes frontend source mutation to `implement-frontend`
and implementation auditing to `audit-frontend`.

Project scope:

```bash
npx skills remove design-ui
npx skills@latest add idaibin/skills --skill design-system
```

Global Codex scope:

```bash
npx skills remove design-ui --global --agent codex
npx skills@latest add idaibin/skills \
  --skill design-system --global --agent codex
```

Other retired names remain mapped as follows:

| Retired | Current |
| --- | --- |
| `repo-context` | `repo-map` |
| `code-review` | `repo-review` |
| `code-delivery` | `repo-delivery` |
| `chatgpt-review-bridge` | `chatgpt-review` |
| `code-planner` | Codex or host built-in planning plus effective `AGENTS.md` rules |
| `diagnose` | Codex or host built-in diagnosis plus effective `AGENTS.md` rules |

## Maintainer Check

Before publishing, verify source discovery from the repository root:

```bash
npx skills@latest add . --list
```

Then run the repository validation commands documented in [README.md](README.md).
