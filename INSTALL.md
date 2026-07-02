# Install Skills

This file is for AI agents or users who want to install or update skills from this repository.

Install only these skill package directories:

- `skills/code-context`
- `skills/code-planner`
- `skills/code-review`
- `skills/code-security`
- `skills/ops-browser`
- `skills/ops-client`

Do not install the repository root, `prompts/`, `docs/`, or legacy skill names such as `repo-context`, `commit-reviewer`, or `planner`.

## Recommended Global Install

Use the standard `skills` npm CLI user-level flow:

```bash
npx skills add https://github.com/idaibin/aicraft -g
```

List available skills without installing:

```bash
npx skills add https://github.com/idaibin/aicraft --list
```

Install selected skills:

```bash
npx skills add https://github.com/idaibin/aicraft \
  -g --skill code-context code-planner code-review code-security ops-browser ops-client
```

For multiple selected skills, pass the names after `--skill` as shown above.

Install only the operations skills:

```bash
npx skills add https://github.com/idaibin/aicraft -g --skill ops-browser ops-client
```

Without `-g`, the `skills` CLI installs into the current project scope.

## Update

Update installed skills:

```bash
npx skills update -g
```

Update only selected skills:

```bash
npx skills update -g ops-browser ops-client
```

For updates, selected skill names are positional arguments.

After installing or upgrading skills, restart any long-running agent app so updated skill metadata and descriptions are loaded.

## Reproducible Project Installs

The `skills` CLI also exposes `skills-lock.json` restore support through `skills experimental_install`. Treat it as experimental for now; prefer the standard install flow for normal use.

## Maintainer Validation

Use this only when developing this repository:

```bash
python3 scripts/validate-skills.py
```

This validates source packages without installing them. End-user installation and updates should use `npx skills add -g` and `npx skills update -g` for global installs.
