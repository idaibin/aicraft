# Blog Restructure Execution Prompt

Use this prompt when turning a blog or personal site into an AI-centered content system. This active prompt is the shorter execution version; historical PRD material should stay outside active prompts and can be recovered from git history or a dedicated archive when one exists.

## Task

[Describe the target blog, current structure, and requested restructuring scope here.]

## Language

- Respond in the user's language unless the user explicitly requests another language.
- Keep route names, collection names, code, commands, paths, and framework identifiers unchanged.

## Inputs

- Site repo path or URL: [provide path/URL]
- Current stack: [Astro / Next.js / other / unknown]
- Current content structure: [provide known collections/routes]
- Required output: [plan only / implementation / review / PRD draft]
- Constraints: [for example: keep Astro, no heavy app behavior, preserve existing content]

If any input is missing, inspect the repository when available. If it is not available, state the gap and produce a plan based only on supplied context.

## Goal

Restructure the site from a generic personal blog into an AI-centered content system that organizes:

- `Signals`: high-value AI updates, trends, and release signals
- `Workflows`: practical AI usage and engineering workflows
- `Prompts`: reusable task prompts
- `Skills`: reusable capability modules and agent-style workflows
- `Notes`: Rustzen, architecture, engineering experience, and long-term notes

## Rules

- Prioritize information architecture over visual novelty.
- Keep the site content-first and lightweight.
- Do not turn the site into a SaaS, dashboard, user system, or heavy client app unless explicitly requested.
- Do not keep old `blog` or `rustzen-admin` structures as first-class navigation if AI is the main story.
- Preserve existing valuable content by migrating it into the new content model.
- Keep topics such as MCP, Agent, RAG, Evals, Tool Calling, and Context Engineering as tags/topics rather than top-level navigation unless there is a clear reason.
- Keep RSS/feed expansion in mind, but do not overbuild it in the first pass.

## Suggested Structure

Top-level navigation:

- Home
- Signals
- Workflows
- Prompts
- Skills
- Notes

Optional or secondary:

- Feeds
- Topics
- About

Recommended routes:

- `/`
- `/signals`
- `/signals/[slug]`
- `/workflows`
- `/workflows/[slug]`
- `/prompts`
- `/prompts/[slug]`
- `/skills`
- `/skills/[slug]`
- `/notes`
- `/notes/[slug]`
- `/feeds`
- `/rss.xml`
- `/signals/rss.xml`

## Implementation Checklist

1. Inspect current repo structure, content collections, routes, layouts, and feed generation.
2. Map old content into the new model:
   - AI updates -> `signals`
   - AI methods and usage patterns -> `workflows`
   - prompt assets -> `prompts`
   - skill/system prompt/workflow modules -> `skills`
   - Rustzen, architecture, product, and engineering notes -> `notes`
3. Redesign the homepage as a content orchestration page, not a chronological post list.
4. Create or update collection schemas, list pages, detail pages, navigation, and feed routes.
5. Keep UI editorial and technical: clear hierarchy, metadata, tags, and practical reading paths.
6. Add lightweight interactions only when useful, such as copy prompt, copy feed URL, TOC, or related reading.

## Output

Return:

1. Current structure summary
2. Proposed information architecture
3. Content migration map
4. Route and collection changes
5. UI and interaction recommendations
6. Implementation steps
7. Verification plan
8. Risks and unresolved questions
