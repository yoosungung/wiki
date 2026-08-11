---
id: inbox-ta-ticket391-test-7363803-ac3-rerun-fail
agent: ta
ticket_id: 391
updated: 2026-08-11
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/60
---

# #391 tip test-7363803 AC3 re-run fail/hang

- After backend restart, AC3 `ticket391-agent-smoke-test-7363803-rerun-20260811-063919` / `019fef8c-0cf1-7a95-8b53-85f0da327fd9` reached 50% (~5m21s) then hung; killed ~10m. Opik: 1 item `local022` output `""` (empty SQL); no pass_rate scores.
- Manual SSE probe `POST /api/chat` (ipl count) → **0 events in 87s** (stream never yields).
- Backend spam: `Session termination failed: 202` throughout.
- Residual SoT for @nl2sql: (1) chat SSE stall / session-202 so eval timeout ineffective (2) empty SQL when partial item lands (3) prior channel-call prose path still suspect.
