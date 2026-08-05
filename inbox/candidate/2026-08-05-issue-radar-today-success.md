---
id: inbox-candidate-2026-08-05-issue-radar-today-success
agent: candidate
ticket_id: 167
updated: 2026-08-05
status: inbox
sources:
  - ticket:167
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
  - wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md
---

# Issue radar → today 성공 (Naver 복구)

- `agent/.env`의 `NAVER_CLIENT_ID`/`SECRET` 로드 후 `issue_radar.py run`(Leantime 플래그 없음) → candidates 7건(score≥4).
- `publish_today.py`로 `wiki/data/today.yaml` 갱신(items=7). 빈 덮어쓰기 아님.
- 커밋 `[agent] update today.yaml 2026-08-05` (`63eb89e`) — today.yaml만.
- `git remote`에 박힌 PAT는 `yoosungung`으로 receive-pack 403; env `GH_TOKEN`(berryking404)으로 push 성공. 원격 URL 토큰과 런타임 토큰 불일치를 분리해 진단할 것.
