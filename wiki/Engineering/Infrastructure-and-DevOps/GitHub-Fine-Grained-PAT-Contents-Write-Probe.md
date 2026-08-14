---
id: github-fine-grained-pat-contents-write-probe
title: "Fine-grained PAT: permissions.push ≠ Contents Write"
status: canonical
owner: km
updated: "2026-08-14"
last_updated: "2026-08-14"
review_after: "2026-11-14"
sources:
  - ticket:50
  - ticket:167
  - https://docs.github.com/rest/git/refs#create-a-reference
tags: ["Infrastructure", "DevOps", "GitHub", "PAT", "RBAC"]
type: "wiki"
---

# Fine-grained PAT: permissions.push ≠ Contents Write

에이전트 Pod의 `GH_TOKEN`이 REST로는 push 가능해 보여도 **git push / refs 생성은 403**인 함정.

## 함정

```bash
# 소유자 관점 capability — PAT 스코프가 아님
gh api repos/<owner>/<repo> --jq .permissions.push   # true 일 수 있음

# 실제 ship 경로 — fine-grained에 Contents: Write 없으면 실패
git push origin HEAD
gh api -X POST repos/<owner>/<repo>/git/refs -f ref=refs/heads/probe -f sha=<sha>
# → Resource not accessible by personal access token (HTTP 403)
```

## 프로브 (ship-ready 증거)

`permissions.push=true`만으로 ship-ready라고 쓰지 않는다. 아래 중 하나로 **쓰기**를 확인한다.

1. `git push` (receive-pack) 성공
2. `POST /repos/{owner}/{repo}/git/refs` 성공
3. fine-grained 토큰에 해당 레포 **Contents: Read and write** (또는 classic `repo`)

## 교차 소유 레포

토큰 identity가 **다른 owner** 레포에 Contents Write가 없으면 동일하게 403이다. 퍼블리시 게이트 PASS와 push 성공을 혼동하지 않는다 — [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]].

## remote URL 임베디드 PAT ≠ 런타임 `GH_TOKEN`

`git remote`에 박힌 토큰(receive-pack 403)과 환경변수 `GH_TOKEN`(다른 identity, 쓰기 OK)이 **불일치**할 수 있다. 진단 시 `git remote -v` identity와 `gh api user` / env 토큰을 분리한다. 게이트 PASS 후 push만 실패하면 이 축을 먼저 본다.

`http.extraheader`에 박힌 예전 토큰과 URL 임베디드 토큰이 겹치면 401이 난다. **tenant override를 remote URL에 넣은 한 번의 push**면 충분하다. extraheader를 남긴 채 재시도하지 않는다.

## 적용 팁

- 로컬 pytest/게이트가 통과해도 PAT 쓰기 없으면 원격 반영이 막힌다 — 게이트 이슈와 토큰 이슈를 분리해 보고한다.
- 토큰 갱신 후 같은 프로브를 다시 돌려야 한다.
- GHCR 패키지 푸시는 Contents와 별축 — [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/GHCR-Actions-Package-Write-ACL.md]]
