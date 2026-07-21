# Candidate Live Trials

This directory records empirical candidate-only workflow trials that are useful for
iteration but do not satisfy the formal behavior/workflow verification gate.

Each record must include:

- source task/thread ID and observation date;
- target repository, branch/worktree state, fixed Git basis, and whether changes are
  committed or still local;
- selected Skill revision or the limitation when the trial used an uncommitted candidate;
- bounded service, feature, operation, authority, real consumer, and product artifact;
- generator/version/command sources plus baseline/candidate artifact provenance;
- results for generation, validation, idempotence, compatibility, generated client,
  duplicate DTO ownership, backend runtime, frontend, runtime UI, CI, and review;
- direct evidence paths/hashes when retained;
- failures, exclusions, `Not found`, and `Not verified` items;
- an explicit catalog decision: revise, repeat, reject, or retain candidate.

These records are not entries in `evidence-manifest.json`. They may inform contract
and eval revisions, but they cannot set `behavior` or `workflow` to `verified` until
the independent semantic-verifier requirements in `validation-plan.md` are met.
