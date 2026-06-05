# AICraft

A focused repository for reusable AI workflow assets: prompts, skills, and packaged context patterns that can be reused, published, or adapted across real projects.

## Goal

AICraft turns repeated AI working habits into durable assets with clear boundaries:

- `prompts/` stores reusable task templates and workflow instructions.
- `skills/` packages stable workflows into portable agent capabilities.
- retired material stays out of the active working set and can be recovered from git history when needed.

The active content should help an agent start with real project context, preserve local changes, follow exact tool and command constraints, verify work, and report results clearly.

## Active Structure

- `skills/`
  - publishable or reusable skill packages
  - each skill keeps its own `SKILL.md`, `agents/`, and `references/` layout

- `prompts/`
  - reusable prompt assets
  - grouped by use case, such as development workflows, automation, agent systems, and project-specific prompts
  - each file should have a clear task boundary, scenario, prompt text, and usage constraints

## Principles

- keep active root content reusable
- keep prompt and skill assets directly accessible
- keep publishable skills self-contained; repo-local prompts can supplement them but should not be required
- let prompts capture task language, and let skills capture stable execution workflows
- retire time-sensitive or old workflow material from the active root
- avoid mixing transient notes and historical references into the active root
