# Usage

Use `writing-editor` when the main job is to turn supplied facts, notes, or a draft into publishable writing with a recognizably human voice.

## Trigger Examples

- `用 writing-editor 把这篇技术博客重写得像我自己写的，保留所有命令和结论。`
- `根据这些真实开发记录写一篇长文，不要补我没说过的经历。`
- `把这段改成 200 字以内的短文，只保留一个观点。`
- `给这个开发者工具写一篇克制的软文，不要编用户评价和数据。`
- `把这篇项目复盘改得更像个人博客，不要汇报体。`
- `把这个教程改成掘金能直接发布的版本，保留版本、命令和验证步骤。`
- `把这篇文章改成知乎回答，先直接回答问题，再展开理由。`
- `把这段产品介绍改成公众号文章，但不要标题党和强行升华。`
- `把这篇复盘改成 Reddit / Hacker News 风格的英文帖子。`
- `找出这篇文章里的 AI 模板、事实风险和口吻漂移。`

## Non-Trigger Examples

- `审查这段 Rust 代码有没有并发问题。`
- `核对这篇新闻里的事实是否准确。`
- `把合同改得更严谨。`
- `统一论文引用格式。`
- `模仿某位在世作家的文风写一篇新文章。`
- `帮我骗过 AI 检测器。`

Route these to the relevant review, research, legal, academic, or creative-writing workflow.

## Mode Selection

| Request | Mode | Default output |
| --- | --- | --- |
| What sounds wrong or AI-like? | Diagnose | Evidence-based issues and editing direction |
| Improve an existing draft | Rewrite | Finished text only |
| Write from notes, logs, or evidence | Draft from source | Finished text only |
| Caption, tweet, announcement, brief opinion | Short-form | Platform-ready text only |
| Product or service article with persuasion | Factual soft copy | Finished copy only |
| Tutorial, architecture note, retrospective | Technical long-form | Finished article only |
| Same content for another platform | Platform adaptation | Target-platform artifact only |

A request can combine modes, such as `Draft from source + Technical long-form + Juejin`.

Load only what the request needs:

- always apply `fact-integrity.md`
- load `content-modes.md` when form changes structure or evidence requirements
- load `platform-calibration.md` only for a named platform adaptation
- load `revision-transparency.md` only for already-published material with substantive changes
- use style references and examples for calibration, never as sources of facts or author experience

## Required Context

Use what the user has already supplied. Infer only low-risk editorial choices such as paragraph length. Do not infer facts.

The useful context fields are:

- source material
- target reader
- purpose
- platform
- desired length
- author sample
- protected text
- desired action
- claims that require verification

When a missing field would change facts or the author's position, return `Not enough context` rather than asking the prose to hide the gap.

## Editing Priority

Use this order:

1. factual and technical integrity
2. author's actual position
3. reader comprehension
4. information density
5. structure and rhythm
6. platform fit
7. surface polish

Do not trade a higher-priority item for a smoother sentence.

## Output Behavior

- Do not announce the workflow.
- Do not explain that the text was "humanized."
- Do not append a change log, score, or offer unless requested.
- Preserve repository frontmatter, links, code fences, and headings when editing a content file.
- When the user asks for multiple variants, make each variant solve a distinct editorial goal rather than swapping synonyms.

## Validation Boundary

`validate-skills.py --quality-report` reports documented Eval coverage. `eval-writing-editor.py` runs deterministic contract fixtures. Neither result proves broad LLM writing quality; model execution and subjective prose quality remain `Not verified` unless separately evaluated.
