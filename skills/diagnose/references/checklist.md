# Diagnose Checklist

Use this checklist when diagnosing a concrete technical failure.

## Execution Boundary

- Keep tracked repository files, the index, checkout, and Git refs unchanged under `diagnose`.
- Treat explain, why, debug, root-cause, investigate, and before-changing-code wording as diagnosis-only authorization.
- When the user also asks to fix, record that implementation is authorized after diagnosis, then transition to the matching implementation skill only after confirming the root cause.
- Record initial and final worktree status, `HEAD`, branch/detached state, index state, and temporary artifacts so the investigation is auditable.

## Required Context

- Read relevant repo guidance first.
- Run `git status --short --branch`.
- Identify the exact symptom, expected behavior, observed behavior, environment, command, URL, input, account state, runtime state, or artifact.
- Read the full error output, stack trace, failing assertion, console message, query plan, profile, or timing data before summarizing.
- Check recent diffs, commits, dependency/config changes, and environment differences when relevant without mutating the target checkout.

## Feedback Loop

- Prefer the smallest agent-runnable loop that can go red and green:
  - failing unit, integration, or end-to-end test;
  - repository command with a focused assertion;
  - HTTP request or script against a controlled environment;
  - CLI invocation with fixture input and expected output;
  - browser or desktop evidence loop coordinated through the matching operations skill;
  - replayed request, payload, trace, or event log;
  - minimal task-owned temporary harness;
  - read-only differential comparison between known-good and known-bad revisions.
- Do not run `git bisect`, checkout/switch/reset, create a worktree, or mutate refs in the target checkout. A separately authorized isolated workflow must leave the target checkout untouched and record initial/final refs.
- Make the loop specific to the user's symptom. A generic command exit code is not enough.
- For flaky failures, loop the trigger, pin seeds/time where possible, stress the suspected path, and report reproduction rate.
- If no loop can be built, report what was tried and the exact missing artifact, access, data, or runtime needed.

## Reproduce and Minimize

- Run or document the exact loop before proposing remediation.
- Confirm the loop catches the same symptom the user reported.
- Remove steps, inputs, callers, configuration, data, viewport, account/cache state, or timing assumptions one at a time when minimization is required.
- Stop minimizing when every remaining element is load-bearing.
- Do not perform elaborate minimization for a fully bounded compiler or deterministic test error.

## Hypothesize and Probe

- Use one strongly evidenced direct hypothesis for bounded deterministic failures.
- For broader failures, rank credible falsifiable hypotheses and state the prediction that distinguishes each one.
- Probe one variable at a time with debugger/REPL inspection, runtime state, targeted logs, traces, profiles, query plans, or focused assertions.
- Use read-only probes or task-owned temporary artifacts. Do not edit tracked files under `diagnose`.
- Tag temporary artifacts and remove or report them before handoff.
- For performance regressions, measure a representative baseline first and keep inputs, build mode, environment, and repetitions comparable.

## Confirm and Hand Off

- Confirm the root cause from the feedback loop and probe evidence, or state the exact `Not verified` gap.
- Define the smallest permanent remediation at the source of the bad value, state, contract, timing, dependency, or ownership boundary.
- Identify the regression test seam that would fail before and pass after the fix.
- When no fix was requested, report the remediation without applying it.
- When a fix was requested, hand off to the matching implementation skill with:
  - confirmed cause and evidence;
  - affected paths/symbols/contracts;
  - bounded implementation scope and do-not-touch paths;
  - original loop and minimized reproduction;
  - regression seam;
  - required validation and remaining gaps.
- The implementation skill applies the change and reruns the original loop plus repository-defined checks.

## Stop Conditions

- Stop when the symptom cannot be reproduced and no adequate artifact or runtime evidence is available.
- Stop when several materially different hypotheses are falsified and each new probe reveals broader architectural coupling; report the concern before expanding scope.
- Stop when a permanent edit would be required and no implementation authorization exists.
- Mark unconfirmed root cause, unchecked runtime behavior, missing regression coverage, or unavailable tooling `Not verified`.
