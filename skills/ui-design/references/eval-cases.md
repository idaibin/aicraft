# Eval Cases

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Design this operations page from the confirmed routes and data, including wireframes, high-fidelity states, responsive behavior, and a frontend handoff.` | Trigger `ui-design` Feature UI profile. |
| `Give this onboarding flow two visual options and specify loading, validation, error, success, focus, and reduced-motion states before code.` | Trigger Feature UI without changing the shared system. |
| `Use the host image generator for three constrained hero concepts, compare them, and keep the result as design evidence only.` | Trigger Feature UI and delegate rendering to the host image tool. |
| `Build three materially different, disposable interaction prototypes to answer whether inline or staged editing fits this one workflow; do not commit them.` | Trigger the Feature UI prototype branch with one question, finite budget, comparison, and disposal boundary. |
| `Our shared Button semantics and spacing tokens must change across four surfaces; update the accepted system with rollback.` | Trigger the conditional Design System profile. |
| `Extract the shared token and component-variant rules already repeated across these representative screens.` | Trigger the Design System profile without claiming screenshots prove runtime behavior. |
| `Evaluate this rendered page against the accepted shared system and the feature-state contract.` | Trigger Feature UI evaluation; load shared artifacts only as evidence. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Implement the accepted page design in React.` | Prefer `dev-frontend`; consume `ui-design` artifacts. |
| `Audit the changed frontend for accessibility and token drift.` | Prefer `audit-frontend`. |
| `Specify this feature's users, permissions, failure behavior, and acceptance.` | Prefer `product-spec`. |
| `Open the page and capture console, network, and screenshots.` | Prefer `ops-browser`. |
| `Launch the Tauri app and prove the real window.` | Prefer `ops-client`. |
| `Commit and push the accepted UI changes.` | Prefer `repo-delivery`. |

## Independent Review Outlet Eval

| Prompt | Expected |
| --- | --- |
| `Finish the Feature UI direction, then explicitly prepare an independent ChatGPT accessibility challenge.` | Keep `ui-design` as owner and emit one lightweight `ask-chatgpt` handoff. |
| `Finish the Feature UI direction from local evidence only; no external review was requested.` | Emit no `ask-chatgpt` handoff. |

## Quality Eval

| Case | Pass evidence | Reject if |
| --- | --- | --- |
| Profile gate | defaults one page/flow to Feature UI and activates Design System only for shared tokens, semantics, variants, or visual-language changes | treats every page as a system redesign |
| Grounding | records product, audience, job, facts, actions, states, current owners, exclusions, and gaps | invents a generic dashboard brief |
| Artifact economy | produces one primary page/flow artifact plus decision-changing dependencies | always creates a full shared package |
| Direction | defines hierarchy, layout, palette, type roles, density, interaction, and one product-rooted signature | applies an interchangeable preset |
| States | covers applicable loading, empty, error, populated, permission, focus, responsive, and reduced motion | approves a single happy screenshot |
| Image-tool boundary | constrains and evaluates host-generated images without claiming tool execution or implementation | pretends the Skill rendered or shipped UI |
| Prototype discipline | names one question, uses materially different comparable options, fixes a finite budget, and preserves a deletion boundary | builds an open-ended mini product, auto-commits, or treats a prototype as runtime proof |
| Shared ownership | references current owners and changes only the necessary shared closure | creates a parallel kit or token layer |
| Evaluation | deterministic blockers precede visual judgment | averages away truth, rights, overflow, or state failures |
| Handoff | supplies concrete layouts, states, interactions, assets, shared deltas, acceptance, and gaps to `dev-frontend` | hands over mood language without implementable decisions |
| Authority | writes design artifacts only and leaves source/runtime/Git work to owners | edits source, operates runtime tools, or commits |

## Scoring

Score each quality case 0–10. Minimum pass: routing is correct, every quality case scores at least 8, no authority violation exists, and applicable shared-package templates validate.
