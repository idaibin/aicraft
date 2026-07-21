# Delivery Report

Use this compact structure after the requested Git state is reached or when delivery stops at a verified blocker:

```markdown
# Delivery Report

## Completed
- <implemented/reviewed/delivered outcome; link existing spec or review>

## Changed Files
- <semantic category, dependency order, exact paths, and resulting commit SHA>

## Verification
- <command or probe>: <result>
- Review: <basis and verdict>
- Commit strategy: <categorized commits|explicit single commit|preserved source commits|squash|explicit partial integration> and <rationale>
- Git proof: <local SHA and remote ref when applicable>

## Known Issues
- <remaining defect, failed check, residual risk, or Not verified gap>

## Next Steps
- <only required or explicitly requested continuation>

## Git Status
- Branch/upstream: <state>
- Commit: <SHA or skipped reason>
- Integration: <source range, target, strategy, and omitted commits or None>
- Remote: <verified ref or Not verified>
- Worktree: <clean or preserved out-of-scope changes>
```

Reference existing artifacts by path or URL instead of copying their full content. Preserve user-provided commit text verbatim in the delivery evidence. Redact tokens, credentials, private payloads, and unrelated personal information.
