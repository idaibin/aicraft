# Automation Task Registry

This registry lists concrete scheduled tasks that consume AICraft standards.

The registry is an index, not the task authority. The target repository task spec remains responsible for repository-specific paths, schema, validation, and commit messages.

## Common Standards

All listed tasks should read:

```text
idaibin/aicraft/docs/standards/cron-automation.md
idaibin/aicraft/docs/standards/github-branching.md
idaibin/aicraft/docs/standards/ai-content-quality.md
```

## AI Signals Commit

- ChatGPT task title: `AI Signals Commit`
- Repository: `idaibin/blog`
- Role: daily long-form AI signals content publishing
- Schedule: daily, 08:00, `UTC+08:00 / Asia/Shanghai`
- Target repository scope: `idaibin/blog/docs/repo-scope.md`
- Task spec: `idaibin/blog/docs/automation/ai-signals-commit.md`
- Writes: `src/content/signals/*.mdx`
- PR: No

Bootstrap prompt should only read the common standards, repository scope, and task spec. Do not duplicate full task rules inside the ChatGPT scheduled task prompt.

## Feeds Hub Update

- ChatGPT task title: `Feeds Hub 更新`
- Repository: `idaibin/feeds-hub`
- Role: short-cycle information feed automation example
- Schedule: hourly, `UTC+08:00 / Asia/Shanghai`
- Target repository scope: `idaibin/feeds-hub/docs/repo-scope.md`
- Task spec: `idaibin/feeds-hub/docs/automation/feeds-hub-update.md`
- Writes: `src/content/<category>/*.md`, `public/images/<category>/*.webp`
- PR: No

Bootstrap prompt should only read the common standards, repository scope, and task spec. Do not duplicate full task rules inside the ChatGPT scheduled task prompt.

Recommended hourly schedule should run at a stable minute, preferably minute `00`, unless rate limits or source update timing require a different minute.
