# AI Content Quality Standard

## Source priority

Use source-backed information. Prefer sources in this order:

1. Primary sources: official announcements, official docs, research papers, arXiv, GitHub repositories, standards bodies, project blogs, company blogs.
2. Reputable reporting: established technology, business, finance, sports, or global news outlets.
3. Secondary summaries only when they link to verifiable primary material.

Avoid unsupported social-media-only claims.

## Evidence rules

Every generated content item must have:

- A clear source name.
- A source URL.
- A concise factual summary.
- A reason why the item matters.
- A clear distinction between confirmed facts, research, releases, rumors, and speculation.

Do not present speculation as confirmed news.

## Freshness rules

For short-cycle feed tasks:

- Prefer the latest verifiable event.
- Use actual event time when available.
- Do not rely only on article publish time when the event time is known.

For long-form blog tasks:

- Prefer durable signals over low-value churn.
- Skip if fewer than the task-specific minimum number of meaningful items is available.

## Deduplication

Before writing content, check:

1. Stable event key.
2. Normalized source URL.
3. Same main entity and same event time.
4. Same product release, match, market event, paper, repository release, or policy update.
5. Whether the new title is only a rewrite of existing content.

A follow-up item is allowed only when it contains a clearly new fact.

## Financial content

Market content may summarize data, news, and risk factors.

Do not provide personalized investment advice.

## Generated images and covers

When a task requires a poster or cover:

- Prefer WebP for realistic feed covers.
- Avoid generic placeholders when the task expects event-specific visuals.
- Do not rely on image-generated text for precise titles, scores, dates, or source names.
- Let the page template or frontmatter provide exact text overlays.
- Do not require exact reproduction of official logos, team marks, real persons, or copyrighted game characters unless the task explicitly has lawful source material and a safe reason.

## Validation

Before commit, verify:

- Required files exist.
- Frontmatter is valid.
- Dates use the required timezone.
- Links are source-backed.
- Markdown or MDX syntax is valid for the target repository.
- Content does not overstate claims.
- Generated content follows the target repository task spec.
