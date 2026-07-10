# Eval Cases

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Audit a TanStack Router Console feature for shadcn reuse, ownership, and query-state boundaries.` | Trigger `audit-frontend`. |
| `Audit the Tauri frontend/Rust boundary for progress, cancellation, errors, menus, and shortcuts.` | Trigger `audit-frontend`. |
| `Check this frontend architecture for duplicated components, stores, services, spacing, and stale docs.` | Trigger `audit-frontend`. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Change one known component's copy and keep everything else unchanged.` | Prefer `implement-frontend`. |
| `Find the unknown cause of this failing frontend test.` | Prefer `diagnose`. |
| `Operate the real Tauri window and capture evidence.` | Prefer `ops-client`. |
| `Review the whole dirty tree and prepare commits.` | Prefer `code-review`. |
| `Review the current frontend diff for component reuse, state boundaries, accessibility, and performance.` | Prefer `code-review`. |

## Scenario Eval

Each scenario must produce the listed investigation, decision, rejection, and
report evidence.

| # | Input scenario | Investigate | Correct decision | Reject | Final report |
| --- | --- | --- | --- | --- | --- |
| 1 | Pages each implement Button, Dialog, Table, and spacing | imports, primitives, variants, tokens, interaction/accessibility differences | identify reuse or composition candidates and stable variants | copy-and-restyle or forced merger of unrelated workflows | candidates, recommended owner, duplicates, validation gaps |
| 2 | New feature directory is unclear | router, adjacent features, aliases, docs, exports, business owner | follow nearest ownership pattern; justify every new layer | new `common/shared` tree for neatness | ownership map, new-file reasons, lifecycle updates |
| 3 | Component is large but splitting adds navigation | responsibilities, change reasons, state/data/layout coupling, tests | keep cohesive or split only at a stable ownership seam | line-count-based extraction | evidence for keeping/splitting and residual complexity |
| 4 | Global store holds local dialog state | consumers, persistence, route/window lifetime, existing local pattern | move local unless durable cross-tree behavior is proven | globalize to avoid props | state class, owner, affected consumers/tests |
| 5 | TanStack route file contains business logic | params/search/loader contract, services, feature workflows, test seams | keep route composition/guards; move stable workflow to owner | empty wrapper layers or router contract changes | route contract preserved, moved owner, generated checks |
| 6 | UI, API helper, and Rust validate a form differently | schemas, transport DTO, authoritative backend constraints, error mapping | align on authoritative contract; share/generate when supported | three drifting rule copies or client-only authority | schema owners, compatibility, field/general error tests |
| 7 | Tauri page invokes Rust on every keypress | call frequency, payload, latency, cache/batch/stream options | debounce/batch/cache or move/subscribe through adapter | direct high-frequency page invokes | before/after path, frequency evidence, native test gap |
| 8 | SQLite task freezes UI without progress | command sync/async, task identity, milestones, cancel path, cleanup | async domain task with real progress, cancellation, terminal states | fake timer progress or uncancellable blocking invoke | channel/events, cancel semantics, real-client verification |
| 9 | Similar pages use inconsistent spacing | shell/page/layout primitives, tokens, duplicated margins/breakpoints | assign one spacing/token owner and remove patches | new per-page magic values | owner, token/primitive reused, responsive visual proof |
| 10 | Agent wants unrelated refactor | request scope, dirty ownership, dependency necessity | exclude unrelated changes and note separately | opportunistic cleanup | exact scope and excluded files/ideas |
| 11 | Project convention conflicts with skill | user request, nearest guidance, existing code/docs, intent | follow rule priority and preserve local contract | enforce external reference or this skill | conflict, winning rule, preserved exception |
| 12 | Code and architecture docs disagree | current runtime/source, docs/indexes, ownership history | identify authoritative evidence and report synchronized remediation scope or blocker | change code only and leave stale docs | mismatches, authority, required files, validation |

## Quality Eval

| Case | Pass evidence | Reject if |
| --- | --- | --- |
| Grounding | reads guidance/status and inventories real route, feature, primitives, data/state, styles, tests, docs | starts from a template |
| Priority | resolves conflicts using the declared order | overrides local conventions with reference-repo choices |
| Reuse | classifies candidates and justifies creation | creates parallel components/layers before search |
| Ownership | assigns page, feature, primitive, hook, service, store, schema, and type responsibilities | uses vague global buckets or ceremonial wrappers |
| State/data | separates state classes and covers applicable lifecycle states | duplicates sources of truth or ignores stale/cancel/retry |
| Layout | uses tokens, one spacing/scroll owner, minimal DOM/CSS, centralized breakpoints | margin patches, duplicate CSS, or forced styling system |
| Performance | traces and measures render/data/bundle/IPC path | default memoization or component-size claims |
| Accessibility | verifies keyboard, focus, labels, non-color and async status | visual-only approval |
| Desktop | uses adapter → command → Rust domain and long-task lifecycle | direct page invokes, blocking work, leaked Rust internals |
| Lifecycle | identifies drift across routes/exports/generated files/tests/docs/indexes and the complete remediation scope | structural code and docs disagree without a finding |
| Scope | preserves unrelated dirty work | performs drive-by cleanup |
| Validation | runs real project commands and runtime proof or reports `Not verified` | invented commands or unsupported success claim |
| Read-only boundary | leaves code and Git state unchanged and routes requested fixes to `implement-frontend` | edits, stages, commits, or claims a fix during the audit |

## Scoring

Minimum pass: score each quality case 0–10. Pass only when trigger/non-trigger routing is
correct and every quality case scores at least 7.
