---
id: inbox-pm-ticket123-agent-ex-smoke-intake
agent: pm
ticket_id: 123
updated: 2026-08-04
status: inbox
sources:
  - ticket:123
  - ticket:122
  - ticket:121
  - ticket:117
  - wiki/Agents/Text-to-SQL/Spider2-Quality-Gate-nl2sql.md
  - https://github.com/yoosungung/nl2sql/blob/main/.factory/quality.yaml
  - spider2-eval/DESIGN.md
---

# T3 agent EX smoke gate intake (#123)

- P1 agent weekly/local EX smoke (local008,local022); Eric: first pass **non-blocking**.
- Depends on T2/#122 (agent wiring); Blocked until T2 Done. Coordinate `opik.command` with T1/#121 gold-sql hard gate.
- Prefer wrapper: `check` → gold-sql hard → agent soft (log + no weekly hard-fail); pass_rate floor deferred.
- tenant_cd/CD N/A; wiki canonical still notes agent as post-spec — update after ship.
