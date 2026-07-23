# Eval Cases

## Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Turn the selected Product Design mockup into an implementation-ready contract for this Token popover, preserving its real data and 338x286 size.` | Trigger `ui-spec` Feature Spec; bind the selected source and specify layout, states, mappings, responsive/accessibility rules, and acceptance without generating images or editing source. |
| `Use this accepted settings screenshot and current components to specify loading, validation, error, success, focus, and reduced-motion behavior before implementation.` | Trigger Feature Spec and label source-derived versus proposed decisions. |
| `Our accepted shared Button semantics, variants, and spacing-token contract must change across four surfaces; specify the revision and rollback.` | Trigger Design System Spec. |
| `Extract the existing token names, component variants, and state vocabulary into the accepted shared contract.` | Trigger Design System Spec extraction without claiming pixels or screenshots prove live semantics. |
| `The shared manifest exists but approval is null; specify this local dialog using verified live owners without promoting the shared baseline.` | Trigger Feature Spec and preserve the approval boundary. |
| `Specify updater failure feedback without hiding the current local archive-operation status.` | Trigger Feature Spec and assign separate feedback owners to the two async domains. |
| `Specify one confirmed dialog from its selected mockup.` | Produce one Feature Spec file, no shared index and no structured manifest. |
| `Specify 18 selected pages spanning home, tasks, contacts, profile, reporting, and settings under one accepted visual language.` | Produce one short shared UI index plus six independently loadable domain contracts, not one omnibus file. |
| `The product behavior and selected mockup are fixed, but mobile overflow ownership is unresolved; challenge that decision before finalizing the UI contract.` | Resolve repository/source facts, ask one bounded UI-contract question with a recommendation and trade-off, then continue only the affected slice. |

## Non-Trigger Eval

| Prompt | Expected |
| --- | --- |
| `Generate three visual directions for this dashboard and let me choose one.` | Prefer the host's Product Design capability; `ui-spec` requires a selected source. |
| `Critique this onboarding flow and produce an improved visual mockup.` | Prefer Product Design audit/ideation. |
| `Build a disposable interactive prototype from this idea.` | Prefer Product Design; do not create prototype code in `ui-spec`. |
| `Implement the accepted UI specification in React.` | Prefer `dev-frontend`; consume `ui-spec` artifacts. |
| `Specify this feature's users, permissions, failure behavior, and product acceptance.` | Prefer `product-spec`. |
| `Audit the implemented frontend for accessibility and token drift.` | Prefer `audit-frontend`. |
| `Map where Button tokens are defined, exported, and consumed without changing their contract.` | Prefer `repo-map`. |
| `Open the page and capture console, network, and screenshots.` | Prefer `ops-browser`. |
| `Commit and push the accepted UI changes.` | Prefer `repo-delivery`. |

## Scenario Eval

| Scenario | Correct decision | Reject if |
| --- | --- | --- |
| One confirmed dialog with one selected source | Produce one Feature Spec file. | Creates a shared index, sibling contracts, JSON, or a manifest. |
| Eighteen confirmed pages across six independent business domains with shared visual rules | Produce one shared UI index plus six independently loadable domain contracts, each with its own complete gates and readiness verdict. | Produces one omnibus specification or eighteen mechanically isolated files with no domain boundary. |
| Several pages only reuse the accepted theme and repository automation does not consume structured UI artifacts | Keep prose Feature Specs and report structured artifacts `Skipped`. | Generates JSON or a manifest because the request is large. |
| A shared token or component semantic changes across surfaces | Activate Design System Spec and generate its structured change/evaluation manifest; create the durable automation manifest only when a verified consumer exists. | Treats the change as local page styling, omits the structured change record, or invents an automation consumer. |
| Some surfaces have selected sources and confirmed facts while others do not | Author only confirmed contracts, list the remaining blockers in the index, give readiness per authored slice, and mark the result `Partial`. | Invents missing contracts, blocks unrelated confirmed slices, or claims `Complete`. |
| A slice lacks required states, interaction, responsive/accessibility rules, or acceptance | Keep that slice not ready and mark the overall multi-surface result `Partial`. | Emits `Ready for dev-frontend <slice>` or package-wide Ready. |
| A contract has both unresolved permission behavior and unresolved focus ownership | Route permission behavior to `product-spec`; challenge focus ownership in `ui-spec` only after the product decision is fixed. | Uses UI questioning to invent product behavior or asks both ownership layers together. |
| The selected source and live component owner answer the apparent UI question | Record the evidence and continue without asking the user. | Interviews the user about a discoverable UI fact. |
| No UI documentation convention exists and one confirmed slice is approved for durable publication | Use `docs/ui/<slice-id>/spec.md` without creating an index. | Adds `docs/specs/`, creates `docs/ui/index.md` for one slice, or creates shared-system artifacts. |
| Several independent UI slices and related PRDs are approved for durable publication | Use `docs/ui/index.md`, `docs/ui/<slice-id>/spec.md`, and matching `docs/prd/<slice-id>/spec.md` links. | Uses unrelated IDs, duplicates PRD facts, or creates an omnibus UI file. |
| Existing repository design location already owns UI contracts | Preserve and use it. | Creates a competing `docs/ui/` tree merely to enforce the fallback. |
| `DESIGN.md` changes after the automation manifest was approved | Fail validation on the semantic-authority SHA-256 mismatch and require a reviewed manifest revision. | Lets automation choose the stale manifest or treats it as an independent authority. |
| A manifest adds token values or visual rules directly | Reject the unknown decision fields; keep those semantics in `DESIGN.md` and bind only declared machine assets. | Accepts the manifest as a second design source. |
| No verified automation consumer exists | Do not create `docs/ui/design-system/manifest.yaml`. | Creates a manifest for documentation symmetry or speculative future use. |
| Named automation consumer file changes after approval | Report a hard consumer conflict until the manifest is deliberately re-approved. | Treats a non-empty consumer label as sufficient evidence. |

## Quality Eval

| Case | Pass evidence | Reject if |
| --- | --- | --- |
| Source gate | records a selected/accepted source with stable identity, revision, approval, rights, use, and ignore boundaries | starts specifying an unselected visual idea or silently invokes image generation |
| Grounding | records product, audience, job, facts, actions, states, current owners, exclusions, and gaps | invents a generic UI contract |
| Evidence precision | distinguishes verified, extracted, proposed, and `Not verified` decisions | treats pixels as exact token, behavior, ownership, accessibility, or runtime proof |
| UI contract challenge | resolves facts first, asks at most one material UI-contract question at a time with recommendation/trade-off/affected slice, stops at slice readiness, and routes product or visual-direction ambiguity | runs a general product interview, reopens accepted visual direction, asks dependent questions together, or exhaustively grills preferences |
| Profile gate | defaults one page/flow to Feature Spec and activates Design System Spec only for shared semantics/contracts | treats every page as a system revision |
| Multi-surface scope | inventories pages, flows, and business domains; one page stays one file, while independent domains use an index plus per-domain contracts | puts independent domains into one large contract or splits one cohesive flow mechanically by page |
| Structured artifact gate | skips JSON/manifest when pages only reuse the accepted theme; emits a structured change/evaluation manifest for Design System Spec changes; emits the durable automation manifest only for a verified consumer | generates JSON because a request has many pages, omits the structured change record, or invents an automation consumer |
| Slice readiness | emits `Ready for dev-frontend <slice>` per complete contract and marks the overall result `Partial` while any requested slice is unconfirmed or incomplete | gives one package-wide Ready verdict or lets one open slice block every confirmed slice |
| Partial authoring | authors only confirmed slice contracts and keeps unconfirmed slices/blockers in the index | invents contracts for unconfirmed pages or claims completion without per-slice states and acceptance |
| Consumer read contract | a developer can load the shared index, target slice, and linked shared-system facts without sibling contracts | requires loading all page contracts to implement one slice |
| Documentation fallback | uses repository convention first; otherwise writes directly under `docs/ui/`, adds an index only for multiple slices, shares slice IDs with PRD, and never adds `docs/specs/` | creates a competing tree, unnecessary index, mismatched slice IDs, or another wrapper layer |
| Design authority | keeps `DESIGN.md` as semantic authority and the manifest as a consumer-named, hash-bound automation contract whose mismatches fail validation | allows two competing authorities, unbound assets, independent manifest decisions, or warn-only conflicts |
| States and interaction | covers applicable states, transitions, feedback ownership, focus, and reduced motion | specifies only the happy appearance |
| Responsive/accessibility | defines reflow, overflow, targets, keyboard/focus, semantics, contrast, localization, and exclusions | hands implementation a desktop screenshot only |
| Reuse mapping | records `reuse`, bounded `adapt`, or justified `new` against live owners | creates a parallel kit or token layer |
| Approval boundary | revalidates live owners and requires approval before shared promotion | treats a pending, rejected, or stale manifest as accepted |
| Handoff | each slice supplies source revision, layouts, states, interactions, assets, mappings, shared deltas, acceptance, gaps, and its readiness verdict to `dev-frontend` | hands over visual mood language, an omnibus package verdict, or a slice missing implementable decisions |
| Authority | writes specification artifacts only | generates/edits images, builds prototypes, edits product source, operates runtime tools, or mutates Git |

## Scoring

Score each quality case 0–10. Minimum pass: routing is correct, every quality case scores at least 8, no authority violation exists, and applicable shared-package templates validate.
