# Eval Cases

Use these cases when changing `domain-modeling` triggers, authority, artifact behavior, output, or routing.

## Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `Before planning code, model Node, Metric, Observation, Alert, Report, and Policy, including their states and rules.` | Should trigger `domain-modeling`. | Explicit concepts, lifecycle, and rules. |
| `Our docs use account, tenant, member, and user inconsistently. Establish one ubiquitous language.` | Should trigger `domain-modeling`. | Terminology conflict. |
| `Map the order state machine, invalid transitions, retries, and cancellation invariants.` | Should trigger `domain-modeling`. | Lifecycle modeling. |
| `Separate billing and entitlement into bounded contexts and show ownership.` | Should trigger `domain-modeling`. | Context-boundary modeling. |
| `Update the existing domain glossary with the decisions we just confirmed, but do not touch code.` | Should trigger Artifact update mode after checking explicit write scope. | Authorized domain-doc write. |

## Non-Trigger Eval

| User prompt | Expected result | Why |
| --- | --- | --- |
| `Map the real repository roots, startup commands, and reusable modules.` | Should prefer `repo-map`. | Repository semantics, not business modeling. |
| `Turn this approved model into technical tasks, dependencies, validation, and reject gates.` | Should prefer `code-planner`. | Executable planning. |
| `Find why the order gets stuck in processing.` | Should prefer `diagnose`. | Concrete failure investigation. |
| `Implement the approved order transition in Rust.` | Should prefer `implement-rust`. | Source mutation. |
| `Review this branch for missing requirements and regressions.` | Should prefer `repo-review`. | Change review. |

## Quality Eval

| Case | Expected evidence | Reject if |
| --- | --- | --- |
| Evidence discipline | Labels confirmed, inferred, conflicting, and unverified statements. | Presents guesses as business truth. |
| Ubiquitous language | Resolves synonyms and overloads per bounded context. | Preserves ambiguous terms without a decision or open question. |
| Concept quality | Separates entities, value objects, commands, events, policies, and actors by identity and responsibility. | Mirrors tables, pages, or classes as the domain. |
| Lifecycle | Defines states, transitions, guards, terminal outcomes, retries, and relevant concurrency. | Lists statuses without transition rules. |
| Business rules | Expresses invariants as observable, testable statements independent of framework/storage. | Mixes implementation decisions into business rules. |
| Boundaries | Creates contexts only from language, ownership, consistency, authority, or source-of-truth differences. | Splits contexts by folder or team name alone. |
| Scenario testing | Probes relevant normal, edge, failure, retry, cancellation, or historical cases. | Produces a tidy model without stress-testing it. |
| Artifact authority | Writes only an explicitly authorized domain artifact and preserves source/Git state. | Edits product code, stages, commits, or writes docs without authorization. |
| Planner boundary | Stops at the domain model and routes technical design/tasks to `code-planner`. | Claims implementation planning ownership. |
| Repository-map boundary | Uses source truth as evidence but routes repository mapping to `repo-map`. | Turns domain modeling into repository onboarding. |

## Scoring

Score each quality case from 0 to 10. Minimum pass: all trigger/non-trigger expectations are correct and every quality case scores at least 8. Artifact-authority violations are hard failures.
