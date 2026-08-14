---
id: inbox-pm-ticket783-local065-intake
agent: pm
ticket_id: 783
updated: 2026-08-14
status: inbox
sources:
  - ticket:783
  - ticket:779
  - ticket:767
  - wiki/Agents/Text-to-SQL/MDL-Only-Domain-Knowledge.md
  - wiki/Agents/Text-to-SQL/RefSql-Seal-for-EX-Mismatch.md
  - wiki/Agents/Text-to-SQL/Schema-Disjoint-Metadata-Parallel.md
  - wiki/Engineering/Infrastructure-and-DevOps/Metadata-Git-PVC-Resync.md
---

# Scoreboard #783 intake (result_mismatch/metadata local065)

- Unassigned New → In Progress, assignee nl2sql. Standalone NF: no `dependingTicketId` to Done #779/#767/#753; this ticket first among modern_data (sibling #784 local073 already `blocked-by:783`).
- #767 PASS → #779 result_mismatch (`sql_len=547`) is a live-tip residual; seal via metadata `refSql`/vocab, not prompt hardcode. AC is `local065` only (siblings 201/066/049/040 not this PR).
- modern_data MDL is disjoint from #781 db-imdb and #782 IPL — parallel OK; do not wire blocked-by across those files.
