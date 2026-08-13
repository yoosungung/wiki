---
id: inbox-pm-698-merge-deploy-test
agent: pm
ticket_id: 698
updated: 2026-08-13
status: inbox
sources:
  - ticket:698
  - https://github.com/yoosungung/nl2sql/pull/86
  - merge_sha:476ec6177ff13642ec4d1669e5707792f5ef1a78
---

# #698 merge → Deploying Test (IPL single master)

- Merged nl2sql#86 (merge_sha `476ec6177ff13642ec4d1669e5707792f5ef1a78`); CI all green.
- Fix: drop unjoined `player_match` from `ipl_match_event`; single master `ball_by_ball`; `player_id`:=`bowler`.
- AC: local020 pass; local023/025 residual RCA documented (not Done until tenant_cd test+qa+aa+prod).
- Board → Deploying Test/@ta for tip roll.
