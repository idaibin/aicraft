# Multi-Surface UI Contracts

Load this reference only when a request covers more than one page, flow, or business
domain.

## Scope Gate

Inventory the requested surfaces before authoring:

- A **surface** is a separately reachable page, modal, panel, or embedded UI region.
- A **flow** is a connected user job whose states and acceptance can be evaluated
  together even when it crosses several surfaces.
- A **business domain** owns distinct behavior, data, actions, failure semantics, or
  acceptance and can be implemented without loading unrelated domain detail.

Several pages remain one UI slice only when they implement one connected job and share
the same product decisions, state model, implementation owner, and acceptance boundary.
Home, tasks, contacts, and profile are separate domains by default even when one shell
or theme contains them.

## Artifact Shape

| Scope | Required artifact |
| --- | --- |
| One page or connected flow | One Feature Spec file |
| Multiple surfaces in one domain | One domain contract when its states and acceptance remain cohesive |
| Multiple independent domains sharing visual rules | One short shared UI index plus one independently loadable contract per confirmed domain |
| Shared token or component semantics change | Design System Spec plus its required structured change/evaluation manifest; add the durable automation manifest only for a verified consumer |

The shared UI index contains only source identity, shared visual facts, domain/surface
inventory, contract links, per-slice status, shared exclusions, and shared dependencies.
Do not repeat each slice's layout, states, interaction, or acceptance in the index.

Each domain contract must independently contain:

1. selected visual-source mapping and `use`/`ignore` boundaries;
2. layout, regions, components, and token mappings;
3. applicable states, transitions, actions, and feedback ownership;
4. responsive, overflow, localization, keyboard/focus, reduced-motion, semantic, and
   accessibility rules;
5. executable acceptance criteria and unresolved blockers.

## Readiness And Partial Results

Evaluate every requested slice independently. Emit `Ready for dev-frontend <slice>`
only when that slice's contract passes all applicable gates. One open slice must not
block unrelated ready slices.

Author contracts only for slices with selected visual sources and confirmed product
facts. List unconfirmed slices and their blockers in the index without inventing their
contracts. Mark the overall result `Partial` when any requested slice lacks a complete
contract, required states/interactions, responsive/accessibility rules, acceptance, or
its own readiness verdict. Use `Complete` only when every requested slice passes.

## Consumer Read Contract

To implement one slice, a consumer reads only:

1. the shared UI index;
2. the target slice contract;
3. any explicitly linked accepted Design System Spec facts.

No slice may depend on the consumer loading every sibling contract. Put a fact in the
shared index only when two or more slices genuinely consume it.

## Structured Artifact Gate

Do not generate JSON, a package manifest, or other structured artifacts merely because
a task has many pages or reuses an existing theme. Generate a structured
change/evaluation manifest when the task creates or changes an accepted Design System
Spec revision. Generate the durable automation manifest only when repository automation
explicitly consumes it. Record the shared-system delta and, when applicable, the real
automation consumer; otherwise report `Structured artifacts: Skipped`.
