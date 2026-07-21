# DevTools Debugging

Use Browser Debug Evidence only for a specified browser-layer failure on
localhost, a LAN development address, a test environment, a public page, or a
production page the user is authorized to inspect.

## Request Readiness

Fix these fields before operating:

- exact URL and environment;
- reproducible action sequence;
- expected behavior and observed symptom;
- relevant viewport, account, storage, cache, or input state;
- requested evidence and the red/green decision it supports;
- allowed state changes and explicit stop conditions.

Route an unexplained or cross-system symptom back to the host diagnosis flow.
Do not use exploratory browser activity to invent a frontend, API, backend, or
database root cause.

## Capability And Evidence Selection

Preflight only the surfaces needed by the request:

| Surface | Direct claims it can support |
| --- | --- |
| DOM/accessibility | rendered elements, semantics, attributes, state, and deterministic selectors |
| CSS/layout | computed styles, box geometry, stacking, clipping, and responsive state |
| Console | client exceptions, warnings, logs, and browser policy errors |
| Network | request URL/method/status/timing, exposed headers, payload, response, and initiator |
| Cookies/storage | browser-visible cookie and local/session storage presence, scope, and changes without exposing secrets |
| Route/resources/cache | navigation, redirects, loaded or failed assets, cache behavior, and browser-enforced CORS |
| Screenshot/viewport | visible state at the recorded viewport and time |
| Upload/download | selected source or resulting artifact and browser-visible transfer state |

If the active browser cannot expose a requested surface, mark that claim `Not
verified` and name the exact trace, HAR, console export, screenshot, or manual
inspection needed. A screenshot does not prove network, storage, or backend
state.

## Red/Green Loop

1. Reproduce the symptom without changing unrelated state.
2. Wait for the relevant hydrated, loaded, or settled page state.
3. Capture the smallest evidence set that proves the red condition.
4. State one falsifiable browser hypothesis.
5. Change one safe variable or run one deterministic observation.
6. Repeat the same steps and capture green, persistent red, or inconclusive evidence.
7. Return direct browser facts, inference labels, missing evidence, and the next owner.

Prefer deterministic DOM, Console, or Network checks and a short repeatable
sequence over exploratory clicking. If reproduction fails, report the attempted
states and missing artifact instead of guessing.

## State Safety And Cleanup

- Treat reload, cache/storage clearing, cookie edits, account or environment
  switching, form actions, uploads, downloads, and production data changes as
  separate operations; perform them only when required and authorized.
- Never reveal cookies, tokens, credentials, private payloads, or unrelated
  account data in retained evidence. Redact sensitive values while preserving
  the facts needed for diagnosis.
- Tag task-only probes, filters, screenshots, traces, and tabs with a task-specific
  identifier. Remove disposable state when safe.
- Retain referenced evidence until it is embedded, archived, transferred, or
  accepted by the caller; then report retained and removed artifacts separately.

## Return Contract

Return the target/environment, Capability Snapshot ID, reproduction steps,
expected and observed behavior, selected evidence surfaces, red/green result,
one-variable experiment, direct browser facts, explicitly labeled inferences,
`Not verified` gaps, state changes, sensitive-data handling, artifact paths or
identifiers, cleanup, and the caller-owned next decision.
