# Diagnostic Feedback Loops

## Selection Order

Choose the highest-fidelity, fastest agent-runnable loop that can detect the user's exact symptom:

1. focused failing test at the real public seam;
2. repository command with a symptom-specific assertion;
3. HTTP or CLI invocation with a known expected result;
4. browser/client evidence delegated to the matching operations skill;
5. replayed request, trace, event, or data fixture;
6. minimal temporary harness;
7. seeded property, fuzz, stress, or repeated-run loop;
8. isolated differential or bisection workflow when separately authorized.

## Readiness Test

Before hypotheses, name one command or bounded operation that:

- has already been run;
- reaches the actual failing path;
- distinguishes the reported bad behavior from expected behavior;
- is deterministic, or reports a useful pinned reproduction rate;
- is fast enough for repeated probes;
- can run without unstructured human interaction.

If this is impossible, report attempted loops and request the missing runtime, capture, fixture, account state, or instrumentation authority. Do not replace missing evidence with a plausible narrative.

## Minimization

Remove one input, step, caller, configuration, state dependency, or timing assumption at a time. Re-run the loop after every removal. Stop when each remaining element is load-bearing. Skip elaborate minimization for a bounded deterministic diagnostic whose owner and failure are already proven.

## Hypothesis Discipline

For each hypothesis, state a prediction that differs from the others. Change one variable per probe. A hypothesis is confirmed only when the predicted evidence appears and competing explanations no longer account for all observations.

For performance, establish comparable baseline inputs, build mode, environment, and repetitions before profiling. For flakes, improve and report reproduction rate rather than claiming deterministic reproduction.
