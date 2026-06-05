# Usage

## What This Skill Does

Commit Reviewer reviews all local git changes before a commit. It inventories real staged and unstaged changes, checks changed code against project structure, coding conventions, related docs, validation commands, and unused-code risks, then groups files by feature intent and drafts exact path-limited staging commands with concise Conventional Commit messages. It can also compare and upgrade this skill from a trusted upstream source.

## When To Use

Use this skill when you need to:

- review all local changes before committing
- check changed code for project-structure, convention, doc, lint, type, build, unused import, or unused definition issues
- split one large change into multiple logical commits
- decide whether a file belongs in the commit or should be excluded
- protect unrelated local changes in a noisy worktree
- produce a clean commit plan with file lists, staging scope, validation, and remaining risk
- update `commit-reviewer` from a GitHub repository, branch, tag, commit, directory, or file URL

## Trigger Keywords

- Direct: `commit-reviewer`, `$commit-reviewer`, `Commit Reviewer`
- Commit review: `提交前审查`, `审查所有改动`, `全量审查`, `检查本地改动`, `提交前检查`
- Commit planning: `分类提交`, `拆分 commit`, `拆分提交`, `生成 commit message`, `Conventional Commit`, `暂存范围`
- Scope control: `只提交当前会话`, `只提交当前上下文`, `只提交本次修改`, `只暂存本次相关文件`
- Upgrade: `commit-reviewer 升级`, `更新 commit-reviewer`, `从 GitHub 更新 skill`, `同步 commit-reviewer`

## What It Outputs

A typical response includes:

- complete local change scope
- change classification
- code review findings, doc/code mismatches, failed checks, unused references, and unverified items
- risks, blockers, and files that should not be committed
- split recommendation by semantic unit
- exact commit plan
- exact `git add` scope for each commit group
- validation already run or still needed
- remaining risk
- upgrade comparison with upstream URL, resolved version, proposed changes, and rejected candidates when using Upgrade mode

Final responses should be concise Chinese by default, unless the user asks for another language.

## Example Prompts

- `Use Commit Reviewer to review my current git changes and split them into clean commits.`
- `Use Commit Reviewer to check this worktree before I commit anything.`
- `Use Commit Reviewer to tell me which files should go into each commit.`
- `审查所有改动，分类提交，只暂存本次相关文件。`
- `只提交当前会话改动；先全量审查，但提交计划只包含当前会话相关文件。`
- `从 https://github.com/idaibin/aicraft 的 main 更新 commit-reviewer，先对比并预览，不要直接覆盖。`

## Non-Goals

- It does not commit automatically unless the user asks it to.
- It does not guess when information is missing.
- It does not include build outputs, caches, logs, or local machine files in commits.
- It does not use broad staging or revert unrelated user changes.
- It does not directly overwrite local skill files from upstream; remote content must be compared and confirmed first.
- It does not replace Repo Context; use Repo Context for repository onboarding, project-map generation, or doc bootstrapping.
