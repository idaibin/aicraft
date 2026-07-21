# ChatGPT Collaboration Profiles

Use this reference after the Codex-first gate determines that an independent ChatGPT web result is requested or required. Theme, ChatGPT capability, and prompt strategy are separate selections. They reuse the same authorization, browser handoff, operation ledger, attribution, and local-verification infrastructure.

## Codex-First Gate

1. Derive the real outcome from the user's natural language; do not require a formal prompt or type selection.
2. Check whether Codex, an existing Skill, or an available host tool can complete that outcome with equal or better evidence. If yes and no independent ChatGPT artifact was requested, use the local owner and stop.
3. Use ChatGPT only for a distinct result: independent challenge, ChatGPT-connected context, Deep Research plan/report, ChatGPT Images artifact, or reviewer-side browser observation.
4. If external use is useful but not explicitly authorized, finish safe local work and request only the missing send/surface authorization.

## Theme Profiles

- **Review:** concrete defects, regressions, missing tests, unsafe assumptions, alternatives, and a scoped verdict against one fixed basis.
- **Repository:** whole-repository architecture, modules, docs, contracts, risks, and contradictions using `github-repository-review.md` and a fixed SHA.
- **Product/domain:** user need, behavior, scope, policy, terminology, business rules, lifecycle, compatibility, and evidence relevant to one decision; never invent domain facts.
- **UI/design:** user task, target surface/device, states, interaction and visual direction, accessibility, reference use/ignore rules, rights/provenance, and acceptance. Separate taste from normative requirements.
- **Architecture:** system boundary, quality attributes, official platform/runtime constraints, contracts, tradeoffs, alternatives, migration cost, and applicability to the fixed repository basis.
- **Implementation/security/delivery:** official API/toolchain behavior, vulnerability advisories, standards, deployment/release constraints, and operational evidence; local verification remains mandatory.
- **Open-ended:** a bounded question that may cross themes; define source classes, exclusions, budget, and stop conditions before external work.

## ChatGPT Capability Selection

- **Standard Chat:** one-off synthesis, prompt refinement, design critique, architecture challenge, or compact independent review.
- **Search:** current or niche facts needing a short cited answer. Do not use it for deep multi-source coverage.
- **Deep Research:** multi-step research that must aggregate sources into a cited report. Supply the desired outcome, source preferences, constraints, and exclusions; inspect and adjust ChatGPT's proposed research plan before it starts.
- **Images:** create or edit a visual only when the ChatGPT Images result is independently requested or required. Record intended use, audience, aspect ratio, source assets, protected content, use/ignore constraints, and acceptance checks.
- **Reviewer browser:** observe declared URLs or web states as supporting evidence. Keep it separate from the transport browser used to operate ChatGPT.

Capability availability is not authorization. Verify the selected capability in the active ChatGPT surface; if unavailable, use an authorized fallback that still satisfies the outcome or stop at Package-only. A Project supplies durable context but is not itself a capability or evidence source.

## Prompt Strategy

- **Direct:** Codex converts the user's request and verified context into one bounded prompt. Use this by default.
- **Plan-assisted:** for broad research, let Deep Research propose its plan, then Codex checks coverage, sources, exclusions, and fit before start.
- **Prompt-refinement chat:** use Standard Chat to improve a prompt only when that draft is an independently useful intermediate result. It is optional, counts as a separate external operation, and never replaces Codex's boundary check.

Every request should contain only what changes the result: outcome, authoritative inputs, theme boundary, selected capability, must-answer questions, source/evidence rules, exclusions, desired artifact, and stop condition.

## Common Contract

1. State one research question, the decision or fixed review basis it informs, the requested date/scope, and explicit exclusions.
2. Prefer primary sources: official specifications, standards, laws/regulations, vendor documentation, source repositories at fixed revisions, original papers/data, and first-party product material. Use secondary sources only to locate or challenge primary evidence and label that role.
3. Require citations with source title/owner, direct URL or immutable revision, relevant section, publication/update date when available, and access date. Distinguish sourced fact, paraphrase, and reviewer inference.
4. Compare sources against the fixed repository basis or a decision basis containing the question, evidence set, date/version, and exclusions. Report agreement, conflicts, applicability limits, stale evidence, and `Not verified` gaps; do not return a detached link dump. A decision basis does not require a Git repository.
5. Treat every conclusion as external advice. Codex verifies actionable claims in the local repository and current authoritative sources before accepting changes.
6. Research never authorizes edits to product facts, domain artifacts, UI assets, source, Git, external systems, or publication. Route separately authorized work to its owner.

## Visual Contract

For Images, return the exact submitted prompt, source-asset identities, generated artifact identity/path, dimensions or aspect ratio, observed completion evidence, edits/variants, acceptance check, and `Not verified` gaps. A generated image is not proof that its depicted UI works or that referenced brand/content rights are cleared.

## Output

Return the Codex-first decision, theme, selected ChatGPT capability, prompt strategy, question or artifact goal, basis/decision relationship, source or asset boundary, external output and attribution, locally verified/rejected implications or acceptance, and `Not found`/`Not verified` gaps.
