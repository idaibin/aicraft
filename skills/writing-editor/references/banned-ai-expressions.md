# AI-Template Pattern Detection

Use this as a diagnostic map, not a replacement dictionary. A phrase is a problem only when it performs no useful job or appears in a cluster of template behavior.

## Pattern Clusters

### Empty framing

Typical signals:

- `随着技术不断发展`
- `在数字化转型背景下`
- `众所周知`
- `本文将从几个方面展开`
- a heading followed by a sentence that merely repeats the heading

Editing move: start with the actual event, question, decision, or task.

### Inflated significance

Typical signals:

- `具有重要意义`
- `标志着关键转折`
- `为未来奠定基础`
- `开启新的篇章`
- `带来无限可能`

Editing move: state what changed in the work, system, or decision.

### Vague authority

Typical signals:

- `业内普遍认为`
- `有研究表明`
- `专家指出`
- `用户一致认可`
- `实践证明`

Editing move: name the source and evidence, qualify the claim, or remove it.

### Symmetric template structure

Typical signals:

- forced `首先 / 其次 / 最后`
- repeated three-item lists
- every section having the same paragraph count
- one benefit sentence followed by one generic example and one summary sentence

Editing move: organize by the actual decision chain. Asymmetry is acceptable when the material is asymmetric.

### Abstract management vocabulary

Typical signals:

- `全面赋能`
- `深度融合`
- `高效协同`
- `能力闭环`
- `生态体系`
- `抓手`
- `方法论沉淀`

Editing move: replace the abstraction with the actor, action, boundary, or observable result.

### Fake depth

Typical signals:

- `真正的问题是`
- `从本质上看`
- `归根结底`
- `值得深思的是`
- `这不仅是 X，更是 Y`

Editing move: make the concrete claim directly. Keep the phrase only when the contrast is real and supported.

### Manufactured drama

Typical signals:

- several one-sentence paragraphs in a row
- repeated `不是...而是...`
- staged punchlines
- aphorisms such as `X 是 Y 的语言`
- fake-candid openers such as `说实话？`

Editing move: restore normal sentence connections and let one detail carry the emphasis.

### Generic positive conclusion

Typical signals:

- `未来可期`
- `值得期待`
- `继续探索更多可能`
- `这只是开始`
- `相信会越来越好`

Editing move: end with the current decision, limitation, next verified step, or unresolved question.

### Promotional gloss

Typical signals:

- `革命性`
- `颠覆式`
- `极致体验`
- `强大而灵活`
- `无缝`
- `轻松实现`
- repeated product name and benefit claims

Editing move: describe the mechanism, evidence, fit, and limitation.

### Chatbot residue

Typical signals:

- `当然可以`
- `希望这对你有帮助`
- `下面让我们深入探讨`
- `如果你愿意，我还可以`
- meta-comments about the rewrite

Editing move: remove the conversation wrapper from the publishable text.

### Fake personal experience

Typical signals:

- a newly invented timeline
- unprovided emotions
- generic `踩了很多坑`
- specific numbers without source
- a polished origin story absent from the notes

Editing move: use only supplied experience. Missing detail stays missing.

### Repetitive recap

Typical signals:

- introduction previews every section
- every section ends with a mini-summary
- final section repeats the introduction and all headings

Editing move: keep the strongest statement once.

## False Positives

Do not flag an item by itself:

- one dash
- one transition word
- one short sentence
- one list
- first person
- polished grammar
- a formal term
- a heading
- a rhetorical question
- an unusual personal phrase

Look for clusters and low-information function.

## Human Signals to Preserve

- exact, hard-to-fabricate details
- mixed feelings
- uncertainty with a reason
- rejected alternatives
- self-correction
- locally natural slang or technical shorthand
- varied sentence length
- a paragraph that is longer because the idea is actually denser
- repetition used deliberately for emphasis

## Decision Rule

For each suspected pattern, ask:

1. What information does this sentence add?
2. Is the wording stronger than the evidence?
3. Does it sound like this author?
4. Does the structure follow the material or a template?
5. Would deleting it lose anything?

Delete, rewrite, or keep based on those answers.
