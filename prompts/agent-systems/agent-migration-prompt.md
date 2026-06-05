# Agent Migration Prompt

Use this prompt when rebuilding an existing AI agent in another account, builder, workspace, or platform.

## Task

Rebuild the source agent as faithfully as possible in the target environment.

## Language

- Respond in the user's language unless the user explicitly requests another language.
- Keep product names, connector names, skill names, system instruction labels, and configuration keys unchanged.

## Inputs

- Source agent name: [provide name]
- Source agent description: [provide description]
- Source system instructions: [provide full or summarized instructions]
- Starter prompts: [provide list]
- Enabled channels: [ChatGPT / Slack / other]
- Memory setting: [enabled / disabled / unknown]
- Web search setting: [enabled / disabled / unknown]
- Connected apps or tools: [GitHub / Notion / other]
- App permission rules: [read-only / write with confirmation / unknown]
- Attached skills: [provide skill names and descriptions]
- Target platform/account: [provide target]

If any required source information is missing, ask for that missing artifact before claiming the migration is complete. Do not invent unavailable system instructions, app permissions, starter prompts, or skill bodies.

## Rebuild Rules

- Preserve the original agent's purpose and behavior.
- Do not redesign the agent unless the user asks for redesign.
- Do not silently merge missing skills into the system prompt and call the migration complete.
- Treat skills as separate reusable capabilities when the target platform supports them.
- If the target platform cannot attach skills, produce functionally equivalent skill specs and clearly mark them as manual rebuild steps.
- Connected app identities usually cannot be copied across accounts; tell the user when manual reconnection is required.
- For tools with write access, preserve confirmation requirements where possible.

## Execution Order

1. Recreate basic agent metadata:
   - name
   - description
   - icon or avatar if applicable
   - channels
   - memory/search settings
2. Recreate system instructions.
3. Recreate starter prompts.
4. Reconnect apps/tools or list manual reconnection steps.
5. Rebuild and attach skills.
6. Compare the rebuilt agent against the source.

## Output

Return:

1. Migration status
2. Recreated metadata
3. Recreated system instructions status
4. Starter prompts status
5. App/tool connection status
6. Skill rebuild status
7. Manual steps still required
8. Differences from the source agent
9. Final verification checklist

## Verification Checklist

- Name and description match.
- System instructions are present.
- Starter prompts are present.
- Memory and search settings match or are documented as unavailable.
- App/tool permissions match or are documented as unavailable.
- Skills are attached or have explicit manual rebuild specs.
- Missing items are listed instead of hidden.
