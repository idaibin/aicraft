# Frontend Behavior-First Development

## Use It When

- behavior and acceptance criteria are stable;
- a public seam can observe the result through a component, route, form, store contract, or browser flow;
- the check can fail for the requested behavior before implementation;
- the repository supports the required test layer or an equivalent focused executable check.

## Do Not Force It When

- exploring visual direction or interaction alternatives;
- changing generated output;
- the only test would assert private state, DOM structure, CSS implementation details, or internal calls;
- a runtime/browser check is the only honest seam and cannot be automated safely in the current environment.

## Vertical Loop

1. Select one acceptance criterion and the highest stable public seam.
2. Add one failing behavior assertion or focused executable check.
3. Confirm it fails for the intended reason.
4. Implement only enough UI, state, data, and styling to pass.
5. Run the focused check and relevant type/lint gate.
6. Refactor only while behavior remains green.
7. Repeat with the next criterion.

Prefer user-visible outcomes and accessible roles over snapshots or internal implementation assertions. Mock only true external boundaries; do not mock the unit whose behavior is under test.
