# Rust Behavior-First Development

## Use It When

- behavior and acceptance criteria are stable;
- a public function, trait boundary, protocol, CLI, service interface, persistence contract, or integration seam can observe the result;
- the check can fail for the requested behavior before implementation;
- the repository test harness can exercise the seam without inventing a parallel architecture.

## Do Not Force It When

- exploring ownership or interface alternatives before the contract is chosen;
- changing generated bindings or mechanically migrating generated code;
- the only test would reach private fields, duplicate the implementation, or mock internal collaborators;
- target, FFI, hardware, or production behavior lacks a representative executable seam in the current environment.

## Vertical Loop

1. Select one acceptance criterion and the highest stable public seam.
2. Add one failing behavior test or focused executable check.
3. Confirm the failure represents the intended behavior, not setup noise.
4. Implement only enough ownership, error, async, persistence, or FFI behavior to pass.
5. Run the focused test and repository format/check baseline.
6. Refactor only while the behavior stays green.
7. Repeat with the next criterion, then run every selected validation overlay.

Expected values must come from the specification, a worked example, protocol contract, or known-good fixture, not from recomputing the implementation under test. Mock true external boundaries; do not mock the module being verified.
