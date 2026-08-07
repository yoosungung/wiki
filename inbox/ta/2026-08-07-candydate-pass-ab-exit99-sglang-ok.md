---
id: inbox-ta-candydate-pass-ab-exit99-sglang-ok
agent: ta
ticket_id: 308
updated: 2026-08-07
status: inbox
sources:
  - ticket:308
  - cluster:llm-serving/sglang-gemma4-12b
---

# Candydate Pass AB exit 99 — SGLang/cluster not the cause

- Ticket 308: Pass AB daily collection `run_id=20260807T030001Z-16385`, `exit_code=99`, wall ~10m (03:00:01Z–03:10:00Z); message: process disappeared before completion status write.
- Node `didim-gpu`: Ready; DiskPressure/MemoryPressure/PIDPressure False at check time; no llm-serving events.
- `sglang-gemma4-12b` 2/2 Running, 0 restarts since 2026-08-06; `/v1/models` 200; no 4xx/5xx in failure window.
- During 03:00–03:10Z pod `…-2wprs` served ≥3 `POST /v1/chat/completions` 200 OK while long decode jobs ran (~7k–19k full tokens, ~85–95 tok/s) — LLM path was live, not crashed.
- Ticket-attached log tail is Pass D from 2026-08-06, not this Pass AB run — host `/tmp/com.candydate.agent.log` for this run_id still needed.
- Hypothesis for candidate: host watchdog/timeout (~600s) while Pass AB waited on long local-LLM generations; not k8s outage.
