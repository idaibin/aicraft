# Frontend Audit Usage

## Trigger Examples

- `Review this Console for duplicate tables, dialogs, spacing, stores, and request mechanisms.`
- `Audit this frontend architecture for component reuse, state ownership, accessibility, performance, and documentation drift; there is no current Git change set.`
- `Check whether this hook, service, or store belongs in the feature or shared layer.`
- `Audit this Tauri frontend boundary for progress, cancellation, errors, menus, and shortcuts.`

## Non-Triggers

- `Change this button label in the known component.` — prefer
  `implement-frontend`.
- `Find why this page crashes.` — prefer `diagnose` until the cause is known.
- `Verify the page in a browser.` — prefer `ops-browser`.
- `Review all dirty files and stage commits.` — prefer `code-review`.
- `Review the current frontend diff for reuse, state, accessibility, and
  performance.` — prefer `code-review`.

## Expected Report

Lead with severity-ranked findings, then report inspected evidence, project
class, reuse candidates, ownership assessment,
state/data/native boundaries, feedback states, token/layout owners,
accessibility/performance evidence, documentation lifecycle, validation, and
residual `Not verified` risks.
