---
id: inbox-ta-unitutor-dns-list-403-soft-skip
agent: ta
ticket_id: f7f980f3-ac59-42fc-a462-45ecfe6df2b8
updated: 2026-10-02
status: inbox
sources:
  - ticket:f7f980f3-ac59-42fc-a462-45ecfe6df2b8
  - https://github.com/yoosungung/UniTutorAI/actions/runs/37014137924
  - https://github.com/yoosungung/UniTutorAI/pull/22
---

# UniTutor Deploy: Zone DNS list 403 soft-skip

- Pages domain `active` + Dashboard CNAME can be live while Actions token lacks Zone DNS Read/Edit → `dns_records` list **403**.
- Hard-failing Ensure after Worker/Pages success blocks Smoke wrongly.
- Fix: soft-skip DNS ensure on list 403; rely on Smoke / Dashboard; grant Zone DNS Edit to re-enable API ensure.
