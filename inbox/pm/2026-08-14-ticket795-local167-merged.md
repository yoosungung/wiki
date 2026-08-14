---
id: inbox-pm-2026-08-14-ticket795-local167-merged
agent: pm
ticket_id: 795
updated: 2026-08-14
status: inbox
sources:
  - ticket:795
  - https://github.com/yoosungung/nl2sql/pull/104
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Semantic-View-Single-Master.md
---

# #795 local167 city_legislation seal merged

- PR #104 merged `merge_sha=ee43ee2a6e7a009d4f282f1e65f42c486f130b7d`. CI run 31788135038 all green.
- Seal `city_legislation_female_first_state_dec31` (female first-state + Dec 31 BETWEEN; gold_b CA/25). Single-master legislator/term/date-dim. MDL only.
- Agent EX pass_rate 1.0. NF tenant_cd N/A → Done. Siblings local169/168/072/070 still RCA-only.
