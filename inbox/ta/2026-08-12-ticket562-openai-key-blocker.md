---
id: inbox-ta-ticket562-openai-key-blocker
agent: ta
ticket_id: 562
updated: 2026-08-12
status: inbox
sources:
  - ticket:562
---

# #562 test overlay OpenAI key blocker

- nl2sql test overlay LLM switch (gemma/SGLang → `openai:gpt-5.4-nano`) needs `nl2sql`/`nl2sql-secrets` key `OPENAI_API_KEY` (real key). At start only `MCP_SHARED_TOKEN` present; CM still `NL2SQL_MODEL=openai:nmilosev/gemma-4-12B-it-quantized.w4a16` + `OPENAI_API_BASE`→sglang + CM `OPENAI_API_KEY=not-needed`.
- Agent policy: secret mutate is destructive — Eric applies key out-of-band; TA then CM patch (`NL2SQL_MODEL=openai:gpt-5.4-nano`, drop `OPENAI_API_BASE` and CM `OPENAI_API_KEY`) + backend rollout + `/api/health`·`/api/ready` evidence. Not a merge_sha tenant_cd image loop; prod overlay out of scope.
