---
id: inbox-pm-2026-08-12-pm-checkpoint-563
agent: pm
ticket_id: 563
updated: 2026-08-12
status: inbox
sources:
  - ticket:563
  - skill:leantime-pm
  - schedule:pm-checkpoint
---

# pm-checkpoint: #563 Deploying Test health-check

- Flow-active only #563 (Deploying Test / assignee ta); IP/Review/QA/DeployProd=0; Approval/misroute empty.
- Silence clock = assignee evidence only; last ta Outcome #2152 @ 08:39Z → ~2.2h (≥2h HC).
- Acted: one @ta health-check add_comment #2802; board #2142 upsert ladder_rung=hc ladder_cycle=1 hc_at=2026-08-12T10:51Z.
- Next run: ≥1h after hc_at with no assignee evidence → skip ARC (assignee=ta) → dead-by-timeout → terminal Approval + admin.
- Note: nl2sql#71 MERGED; #72 OPEN CONFLICTING — does not reset silence; TA should not wait on #72.
