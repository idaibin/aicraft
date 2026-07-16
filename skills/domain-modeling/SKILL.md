---
name: domain-modeling
description: "Use when a product or business domain needs explicit language, entities, relationships, state transitions, invariants, business rules, or bounded contexts before planning or implementation."
---

# Domain Modeling

## Overview

Build an evidence-backed domain model that gives users, specifications, code, and tests one precise language. Model the business problem and lifecycle; do not turn the result into a technical architecture or implementation plan.

## Workflow

1. Read effective repository and host guidance, then inspect only the supplied requirements, existing domain docs, contracts, representative code, and tests needed to understand the named domain.
2. Run `git status --short` before any authorized artifact write and preserve unrelated changes.
3. Establish the modeling scope, actors, goals, in-scope scenarios, excluded scenarios, and unresolved terms.
4. Inventory candidate terms and challenge synonyms, overloaded words, implementation names, and conflicts between docs, code, and user language.
5. Identify entities, value objects, events, commands, policies, and external actors only when evidence gives each a distinct responsibility or invariant.
6. Map relationships, ownership, cardinality, identity, and lifecycle. Use a state machine when behavior depends on state or transition order.
7. Stress-test the model with normal, edge, failure, retry, cancellation, concurrency, and historical-data scenarios that are relevant to the domain.
8. Record business rules as testable statements. Separate confirmed rules, inferred rules, decisions, open questions, and contradictions.
9. Define bounded contexts and context relationships only when terminology, ownership, or consistency rules materially differ.
10. Check the model against requirements and representative code. Report drift instead of silently choosing one source as truth.
11. Return the model in the output contract. Write or update a domain artifact only when the user explicitly requests it, using the repository's existing location and format when available.

## Modes

- **Terminology pass:** resolve a ubiquitous language and conflicting terms.
- **Lifecycle pass:** model states, transitions, guards, events, and terminal outcomes.
- **Boundary pass:** separate contexts, ownership, consistency, and external dependencies.
- **Artifact update:** apply an explicitly authorized domain-doc change without editing product code or Git state.

## Do Not Use For

- Repository roots, commands, runtime boundaries, or reuse inventory; use `repo-map`.
- Technical design, implementation tasks, dependencies, or validation gates; use `code-planner` after the domain is sufficiently clear.
- Root-cause investigation of a failure; use `diagnose`.
- Source implementation or refactoring; use the matching `implement-*` skill.
- Review findings or Git delivery; use `repo-review` or `repo-delivery`.

## Hard Rules

- Do not invent domain facts to complete a tidy diagram.
- Do not use database tables, UI pages, API endpoints, classes, or folders as entities unless they represent a real domain concept.
- Do not collapse actors, identities, resources, observations, commands, events, and policies merely because current code combines them.
- Keep business rules independent of framework, storage, transport, and deployment choices.
- Mark conflicting evidence and request a decision when the conflict changes identity, lifecycle, ownership, money, permission, or irreversible behavior.
- Do not write domain docs without explicit authorization; never edit product source, stage, commit, or push.
- Use `Not found` for missing sources and `Not verified` for unchecked rules or runtime behavior.

## Output Contract

Return scope and evidence sources, glossary, entities/value objects, relationships, state machine, business rules/invariants, bounded contexts, scenarios tested, contradictions, decisions, open questions, and `Not verified` gaps. Distinguish confirmed facts from inference. If an artifact was authorized, report its exact path and the preserved Git state.

## References

- See [references/usage.md](references/usage.md) for triggers and routing examples.
- See [references/modeling-guide.md](references/modeling-guide.md) for the modeling checklist and output template.
- See [references/eval-cases.md](references/eval-cases.md) for trigger, non-trigger, and quality evals.
