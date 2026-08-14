---
id: inbox-pm-scoreboard-752-metadata-mismatch-intake
agent: pm
ticket_id: 752
updated: 2026-08-14
status: inbox
sources:
  - ticket:752
  - ticket:751
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md
---

# Scoreboard #752 intake (result_mismatch/metadata)

- Weekly smoke `local008` (Baseball) / `local022` (IPL) **regressed** to result_mismatch after #751 (SQL emitted, EX vs gold fail) — AC is restore those two, not n=67.
- Domain fix stays in tip MDL (`description` / `refSql` / view / relationship); do not hardcode schema metrics in agent prompts.
- Baseball vs IPL vs modern_data MDL paths are disjoint → #753 can parallel; IPL files overlap #754 sql_exec → serialize IPL after #752.
- Do **not** `dependingTicketId` link improve tickets under a Done scoreboard parent (#751) — that reopens Parent-Done-Requires-Closed-Subtasks.
