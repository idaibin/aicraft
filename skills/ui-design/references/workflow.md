# UI Design Workflow

## Contents

1. Evidence boundary
2. Profile gate
3. Direction and state pass
4. UI prototype branch
5. Artifact pass
6. Evaluation and handoff

## Evidence Boundary

Record confirmed product facts, available data/actions/states, current components and tokens, explicit exclusions, and unresolved questions. Screenshots prove appearance only. DOM, source, API, console, network, accessibility, and native-window claims require their own evidence.

## Profile Gate

Choose **Feature UI** unless the answer to at least one question is yes:

- Must a shared semantic token be added, removed, or redefined?
- Must a reusable component's meaning, public variant contract, or state vocabulary change?
- Must several surfaces adopt a changed visual language or shared rule?
- Is an accepted shared-system owner being created, extracted, maintained, or evaluated?

If not, reference existing owners and keep the work local to the page or flow. If yes, load the Design System artifact contract and change only the shared closure.

## Direction And State Pass

Define the surface's single job, hierarchy, layout/scroll owner, density, palette, type roles, material, interaction tone, responsive behavior, target sizes, focus, reduced motion, realistic content, and relevant loading/empty/error/populated/permission states. Spend visual boldness on one product-rooted signature and remove unsupported decoration.

## UI Prototype Branch

Use a prototype only to answer one named visual or interaction question that static artifacts cannot settle. Fix a finite time/variant budget, produce at least two materially different options when comparison is the point, expose them through one simple comparison surface, and make the options disposable. Each variant must differ in a decision that could change the chosen direction—not only color or decoration. Record the question, constraints, comparison criteria, observed answer, and what may be deleted.

A UI prototype is design evidence, not production implementation. It never authorizes commit, push, publish, persistence, a parallel app architecture, or automatic promotion into source. Logic/state prototypes remain conditional experiments owned by the relevant product, domain, or technical decision workflow; they do not expand `ui-design` ownership.

## Artifact Pass

| Profile | Primary artifact | Optional dependencies |
| --- | --- | --- |
| Feature UI | one page/flow design brief with wireframes or high-fidelity views | bounded prototype, generated assets, comparison record |
| Design System | changed accepted shared artifact | affected tokens/components, references, evaluation, rollback manifest |

Produce only what changes the design or implementation decision. Image rendering remains a host-tool action. A shared manifest is required only when establishing or changing an accepted Design System revision.

## Evaluation And Handoff

Run deterministic truth, rights, required-state, overflow, target-size, reduced-motion, and implementation-budget gates first. Then compare product truth, task completion, information hierarchy, visual coherence, interaction, engineering fit, and evidence completeness. Hand the selected artifacts and unresolved gaps to `dev-frontend`; request runtime evidence from `ops-browser` or `ops-client` after implementation.
