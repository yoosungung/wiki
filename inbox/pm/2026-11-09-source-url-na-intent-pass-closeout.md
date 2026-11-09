---
id: inbox-pm-source-url-na-intent-pass-closeout
agent: pm
ticket_id: 38f15177-82cb-43c9-a7e0-549e9fda9a60
updated: 2026-11-09
status: inbox
sources:
  - ticket:38f15177-82cb-43c9-a7e0-549e9fda9a60
  - https://github.com/berryking404/candidate.win/pull/22
  - https://wiki.candidate.win/people/i-si-ba/
---

# source URL N/A — Pass A/quality_gate + render secondary

- Tier1 quote `source_url="N/A"`가 truthy라 crawl fallback을 가리던 것이 원인. `is_valid_source_url`(http/https만)로 Pass A·quality_gate Rule1 강등.
- 유효 URL 없으면 stance 줄 생략; 기존 `[출처](N/A)`는 **미확인**으로 정리.
- Hugo `render-link.html` 가드는 secondary(비-URL destination → 텍스트만).
- Intent pass 후 PR #22 squash merge → Pages success → prod `href=N/A` 소거 확인.
