# Chinese Technical Writing Style

## Sentence Level

Prefer a visible subject and action.

Weak:

```text
通过相关能力的建设，实现了整体流程的进一步优化。
```

Better:

```text
我把搜索、核验和写入拆成三个步骤，失败时更容易知道卡在哪里。
```

Use simple verbs when they are accurate:

- `是` instead of `作为`
- `有` instead of `具备`
- `改` instead of `进行调整`
- `查` instead of `开展排查`
- `减少` instead of `实现降本增效`

Do not remove technical nouns merely to sound casual. Precision outranks colloquiality.

## Rhythm

- Mix short and long sentences according to idea density.
- Use a short sentence to mark a real decision, not every paragraph.
- Break a paragraph when the reader's task changes, not at a fixed sentence count.
- Allow a parenthetical or aside when it belongs to the author's voice.
- Do not manufacture fragments or punctuation quirks.

## Paragraph Function

Each paragraph should mainly do one job:

- establish context
- make a claim
- provide evidence
- explain mechanism
- show a tradeoff
- transition because the reasoning changes
- record a decision

A paragraph that only announces the next section usually should be deleted.

## Technical Terms

- Keep established English terms when translating would reduce precision.
- Define a term once when the target reader may not know it.
- Use one term consistently; do not cycle synonyms for variety.
- Keep code identifiers, commands, paths, and config exact.
- Put code near the claim it supports.

## Lists

Use a list when items are genuinely parallel or need scanning.

Avoid lists when:

- the items form a causal argument
- every bullet needs a paragraph of explanation
- the list exists only to look comprehensive
- the prose would be shorter and clearer

Do not automatically bold the first phrase of every bullet.

## Headings

Headings should tell the reader what changes in the section.

Prefer:

- `我为什么放弃每个仓库单独配置身份`
- `includeIf 的匹配条件`
- `这套方案解决不了什么`

Avoid:

- `背景`
- `优势`
- `价值`
- `未来展望`
- `总结与思考`

Generic headings are acceptable only in formal documentation where predictability matters more than voice.

## Openings

Useful openings include:

- the exact problem
- a surprising observation supported by evidence
- a decision and its reason
- a short scene from the work
- the result the reader will reproduce

Avoid broad history, market trends, and motivational framing unless they are essential evidence.

## Endings

End when the article's job is complete.

Good endings can be:

- the current decision
- the cost accepted
- the limitation
- the next concrete verification
- a question the author genuinely has not resolved

Do not add inspiration, `未来可期`, or another full summary.

## Personal Judgment

A strong personal sentence names its scope:

```text
对我这种需要同时维护个人和公司仓库的开发者，这比每个仓库手动改 user.email 更稳。
```

A weak universal sentence hides the scope:

```text
这是所有现代开发者都必须掌握的最佳实践。
```

Keep `我认为`, `在这个项目里`, and `目前` when they prevent overclaiming. Remove them only when the sentence remains equally accurate.
