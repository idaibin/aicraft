# Generate AI Research Digest

任务名称：
Generate AI research digest

执行时间：
每天 09:00

时区：
Asia/Shanghai

任务类型：
定时搜索 + 摘要生成

Prompt：
Search the web for recent high-signal AI engineering content from the last 1-3 days when possible.

Focus topics:
- coding agents
- prompt engineering
- context engineering
- agent workflows
- tool use
- function calling
- evals
- skills
- plugins
- specs
- AI-assisted software engineering
- retrieval / planning / execution patterns
- AI infrastructure
- GPU / accelerator updates
- inference stack and deployment economics

Watch entities:
- OpenAI / Codex
- Anthropic / Claude
- Google / Gemini
- Alibaba / Qwen
- Zhipu / GLM / Z.ai
- Moonshot / Kimi / Kimi Code
- Xiaomi / MiMo
- MiniMax
- DeepSeek
- GitHub Copilot / GitHub Engineering
- LangChain / LangGraph
- Vercel AI SDK
- MCP / tool calling / agent runtime ecosystem
- NVIDIA
- domestic GPU / AI chip ecosystem such as Huawei Ascend, Cambricon, Moore Threads, Iluvatar, Biren

Source priority:
1. official docs
2. official blogs / changelogs
3. papers / technical reports
4. engineering blogs
5. high-quality GitHub repositories
6. official infrastructure / chip vendor docs and release pages

Hard exclude:
- marketing
- hype
- generic summaries
- reposts
- low-information content
- no engineering value

Selection rules:
- keep 3-8 items only
- allow fewer if quality is low
- keep only items with practical engineering value
- deduplicate aggressively and keep the strongest original source
- for GPU or infra updates, keep only if they materially affect training, inference, context scaling, tool use, cost, latency, deployment shape, or agent reliability

For each selected item, include:
- Title
- Source
- URL
- Date
- Type
- Tags
- Key Takeaways
- Engineering Implications
- Reusable Suggestions

Then write:
- Key Conclusions
- Observations
- Promotion Candidates

Output language: Chinese
Style: concise, technical, engineering-oriented
