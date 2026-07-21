# Resolving Merge Conflicts

Load this reference only when an authorized merge or rebase is already in progress, or the requested delivery target explicitly requires starting one after branch/divergence checks.

## Intent-First Resolution

1. Fix the current merge/rebase state, conflicted paths, target/source revisions, repository rules, and separately authorized actions: resolve files, stage resolutions, continue/commit the operation, and push.
2. For each conflict, trace both sides to their primary intent: the originating requirement/commit and the current owner, callers, tests, generated sources, migrations, or docs.
3. Resolve one hunk at a time. Preserve compatible intent from both sides; do not pick ours/theirs merely to clear markers.
4. Search the resolved file and affected closure for conflict markers, stale names, duplicate declarations, and structural lifecycle gaps.
5. Run the smallest checks that cover the resolution, then applicable repository gates.
6. If staging is authorized, stage only resolved conflicted paths/hunks and inspect the cached diff. Continue or commit the current merge/rebase only when that action is separately authorized; otherwise stop with the resolved files or index in the requested state.

Abort remains a valid safety action when the basis, intent, permissions, or preservation plan cannot be established. Never derive staging, continuation, commit, push, force-push, cleanup, or branch-deletion authority from permission to resolve conflicts.

## Report

Report the operation and revisions, conflicted paths, intent evidence per hunk, resolution, validation, staged state, whether the merge/rebase was continued or stopped, and every `Not verified` gap.
