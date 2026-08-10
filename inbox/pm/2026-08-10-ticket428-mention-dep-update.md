---
id: inbox-pm-2026-08-10-ticket428-mention-dep-update
agent: pm
ticket_id: 428
updated: 2026-08-10
status: inbox
sources:
  - ticket:428
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/47
---

# #428 mention — dependency advanced, still Blocked

- QA @pm mention (standby / unassigned-triage lineage): #428 remains Blocked; product evidence still waits on #391 Done.
- Live check 2026-08-10: PR #47 MERGED (merge_sha `bede6263b8f31a527e6ba01b5b03b537d013354e`); #391 status=Deploying Test(11) assignee=ta — prior #428 comments that said PR OPEN / Review are stale.
- Closeout unchanged: after #391 full CD Done (Test→QA/AA→Prod), @qa re-runs `cd spider2-eval && uv run spider2-opik weekly`; agent smoke pass_rate>0 → #428 Done + evidence.
