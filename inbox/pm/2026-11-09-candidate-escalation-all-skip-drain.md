---
id: inbox-pm-2026-11-09-candidate-escalation-all-skip-drain
agent: pm
ticket_id: 33e86038-beb9-463e-bbc3-6bcc43dec197
updated: 2026-11-09
status: inbox
sources:
  - ticket:33e86038-beb9-463e-bbc3-6bcc43dec197
  - wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md
---

# candidate.win escalation drain — all-skip closeout

- Pass A 후 `agent/.cache/escalation/pending.jsonl` drain은 usable 0이어도 pending→processed 이동이면 AC 충족(PR/`agent:stances` 불필요).
- 2026-11-09 스킵 분포: `no_source_url` 7 · `no_person_mention` 3 · `no_stance` 2 · `weak_attribution` 1 · `misattribution` 1 (합 14).
- 근거 URL·인물 멘션 없는 Tier1 저신뢰 행은 wiki에 쓰지 않는 것이 스킬 정본; closeout은 건수·사유 표 + `test:`/`wiki:` 마커면 충분.
