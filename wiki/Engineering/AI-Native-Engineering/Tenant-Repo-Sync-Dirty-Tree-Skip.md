---
id: tenant-repo-sync-dirty-tree-skip
title: "tenant-repo-sync: dirty working tree → skip sync (no stash)"
status: canonical
owner: km
updated: "2026-11-03"
last_updated: "2026-11-03"
review_after: "2027-01-05"
sources:
  - inbox/qa/2026-11-02-qa-bulk-weekly.md
  - inbox/aa/2026-11-02-aa-clean-weekly.md
  - inbox/qa/2026-10-26-qa-bulk-weekly.md
  - inbox/qa/2026-10-05-qa-bulk-weekly.md
  - inbox/qa/2026-10-19-qa-bulk-weekly.md
  - schedule:qa-bulk-weekly
  - schedule:aa-clean-weekly
  - schedule:ta-load-weekly
tags: ["Engineering", "AI-Native", "Factory", "NF", "Sync"]
type: "wiki"
---

# tenant-repo-sync: dirty working tree → skip sync (no stash)

주간 NF(`qa-bulk-weekly` / `aa-clean-weekly` / `ta-load-weekly`)는 레지스트리 엔트리마다 `tenant-repo-sync`로 tip을 맞춘다. **워킹트리가 dirty면 sync를 강제하지 않고 skip**한다(stash·reset 금지).

## 규칙

1. `git status`가 dirty(예: `package.json`/`package-lock.json`에 플랫폼 optional dep 추가) → **skip sync** + HEAD/path/`project_id`를 리포트에 남긴다.
2. dirty를 지우려고 stash/hard-reset하지 않는다 — persona workspace leftover는 운영자가 정리.
3. skip sync ≠ 게이트 실패. `.factory/quality.yaml` 부재로 게이트도 skip이면 **NF=0**이 정상([[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]).
4. behind `origin/main`만으로 sync를 강제하지 않는다 — dirty가 해소된 다음 런에서 ff/reset 한다.

## 2026-10-05 사례 (qa)

- `repo_id=sw-factory` dirty: `@rollup/rollup-linux-arm64-gnu` add → skip sync; HEAD behind origin/main by 59.
- crewrp / uni-tutor: clean sync 후 모두 `quality.yaml` 없음 → bulk_api/opik skip; factory `/api/health` 200만 스모크.

## 2026-10-19 사례 (qa)

- `repo_id=sw-factory` dirty: `package.json`/`package-lock.json` → skip sync (no stash); tip `8e6f8af`는 origin만 조회.
- crewrp / uni-tutor: clean sync (`d27b67c` / `73178e8`) 후 `quality.yaml` 없음 → bulk_api/opik skip; factory `/api/health` 200 `qa: pass`.

## 2026-10-26 사례 (qa)

- `repo_id=sw-factory` dirty: `package.json`/`package-lock.json` + `@rollup/rollup-linux-arm64-gnu` → skip sync (no stash); HEAD behind origin/main (origin tip `8e6f8af`는 origin-only).
- crewrp / uni-tutor: clean sync 후 `quality.yaml` 없음 → bulk_api/opik skip; factory `/api/health` 200 `qa: pass`.

## 2026-11-02 사례 (qa / aa)

- 레지스트리 4 repo (`sw-factory` / `crewrp` / `sql-mcp` / `rhwp_batch`; `uni-tutor`는 레지스트리 밖).
- `qa-bulk-weekly`에서 `sw-factory` dirty (`package.json`/`package-lock.json`, no stash, HEAD `690c726` behind `origin/main` `8e6f8af` by 72) → skip sync (`origin/main`도 `quality.yaml` 부재).
- `crewrp` (`47f0340`), `sql-mcp` (`37da574`), `rhwp_batch` (`642974c`): clean sync 후 `quality.yaml` 없음 → `bulk_api`/`opik`/`clean_code` skip; factory `GET /api/health` 200 `{"ok":true,"service":"sw-factory-workers"}`.

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
