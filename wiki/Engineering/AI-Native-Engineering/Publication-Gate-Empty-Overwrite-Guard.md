---
id: publication-gate-empty-overwrite-guard
title: "퍼블리시 게이트 + 빈 산출물 덮어쓰기 금지"
status: canonical
owner: km
updated: "2026-08-17"
last_updated: "2026-08-17"
review_after: "2026-11-17"
sources:
  - ticket:474
  - ticket:854
  - ticket:882
  - ticket:892
  - ticket:929
  - ticket:940
  - schedule:publication-safety
  - schedule:issue-radar
  - ticket:167
  - ticket:340
  - ticket:341
  - ticket:357
  - ticket:367
  - ticket:368
tags: ["Engineering", "AI-Native", "Publish", "Safety", "Git"]
type: "wiki"
---

# 퍼블리시 게이트 + 빈 산출물 덮어쓰기 금지

공개/공유 데이터 파일을 자동 커밋하는 잡에서 **게이트 통과 ≠ push 가능**, **수집 실패 ≠ 빈 파일로 덮어쓰기**를 분리한다.

## 1) Pre-push publication gate

```bash
# 개념: origin/main 대비 워킹트리/ahead 커밋 검사
python agent/publication_gate.py --base origin/main
# exit 0 = PASS, exit 2 / PUBLICATION HOLD = hold (push 금지)
```

게이트 PASS 후에도 git push 403이면 **자격 증명/ACL 문제** — [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]] (remote 임베디드 PAT vs env `GH_TOKEN` 불일치 포함).

## 2) Empty overwrite guard

외부 API/시드 확장이 비어 점수 미달 → `candidates=[]` / `items=[]`일 때:

- **공개 큐 파일을 빈 내용으로 커밋하지 않는다** (마지막 정상 생성분을 보존).
- 원인(미설정 env, 쿼터, 스키마)을 로그·티켓에 남기고 재실행 조건을 명시한다.

## 적용 체크

1. 게이트 스크립트가 CI/스케줄 **push 직전**에 있는가?
2. “변경 없음 / 빈 결과”와 “안전한 갱신”을 구분하는가?
3. push 실패를 게이트 실패와 혼동하지 않는가?

## 분기·스택 운영

- 로컬 `main`이 미공개 Pass 스택으로 `origin/main`과 diverge면, curation/radar 잡은 **`origin/main`에 detach → 작업 → `push HEAD:main` → 로컬 스택 checkout**으로 보존한다. Pass 스택을 curation에 ff-only merge하지 않는다. dirty leftover `agent/cron/` WIP가 이미 PR로 들어갔으면 ff-only pull 전에 정리. preserve branch는 백업일 뿐 ship 경로가 아니다.
- **대안 (스택을 살린 채 ship)**: `git branch agent/pass-stack-preserve-YYYYMMDD`로 백업한 뒤 `origin/main`에 rebase(충돌 0이면 콘텐츠 게이트 → ship). rebase 충돌이 있으면 detach 경로로 되돌린다.
- Pass 스택 rebase/fixup 후 people slug가 바뀌면 **stance·링크를 remap**하고 깨진/org/unknown stance 라인은 drop한 뒤 게이트를 다시 돌린다.
- **검색엔진 결과 URL은 allowlist 출처가 아니다** — 게이트 PASS 이후에도 검색 URL 출처는 공개 본문에서 제거한다.
- **약한 중립(weak-neutral)**: 신원·SSoT가 부족한 stance는 hold만 하지 말고 **drop**. org/unknown·SSoT-없는 slug와 같은 축.
- yaml↔wiki orphan 0을 유지하려면 stub yaml 추가 시 **최소 wiki stub도 같이 seed**. SSoT 카운트는 `yaml==wiki`로 맞춘다.
- **게이트 PASS ≠ content-safe**: `/people/unknown`, org-as-person stance, 이슈 slug를 인물로 쓴 stance, 약한 중립(발언 미확인), 역할·신원 오인 stub는 추가 strip. people promote는 allowlisted 공식/프로필 URL(≥1)이 있을 때만; wiki-only·비허용 호스트는 부족. 애매한 기자·동명이인·역할 불일치·비인물(학교·부처 등)은 hold.
- **동명이인 함정**: allowlist 호스트 URL이 **다른 사람**(같은 이름, 다른 직)이면 콘텐츠 안전 실패 — 그 URL을 promote에 붙이지 않는다.
- **직원명단 미기재**: 성명이 직원명단/조직도에 없으면 `go.kr` 등 허용 호스트여도 승격 근거로 쓰지 않는다.
- **people slug remap**: collapse/접두 규칙(`lee→i`, `park→bak`, `kim→gim`, `jung→jeong`) + `name_ko` 매칭으로 정규화한 뒤 stance·링크를 고친다(예: unknown 김기재 → `gimgijae`). **로마자 비정규 slug**도 같은 축 — 로마자만 보고 유지하지 말고 `name_ko`로 remap.
- **stance 링크는 yaml+wiki 동시 존재 필수**: 한쪽에만 있으면 orphan/깨진 링크. remap·drop 후 yaml↔wiki orphan 0을 재확인한다.
- 공개 전 제거: placeholder/unknown·SSoT 없는 slug·불완전 신원 stub·기관을 people로 링크한 stance.
- Pass D가 people YAML을 추가하면 **최소 wiki stub도 같이 seed**해 yaml↔wiki orphan 0을 유지한다. 약한 중립 줄을 drop해도 orphan 0을 깨지 않게 stub를 함께 맞춘다.
- `http.extraheader` + remote에 박힌 토큰이 401이면, env 토큰을 URL에 넣은 **한 번의 push**로 충분하다 — [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]].
- meta/stub+stance만 갱신하는 잡에서 사이트 빌드 바이너리(예: Hugo)가 없으면 **빌드를 스킵**해도 된다 — 게이트·pytest가 정본이다.
- issue-radar → today 발행: empty-overwrite guard 통과 후에만 공개 큐(`today.yaml` 등)를 커밋·push하고, **승인 티켓은 만들지 않는다**. 캐시 타임스탬프를 남긴다.
- **공개 today 큐는 중립만**: 내부 승인 상태·스케줄/도구명을 노출하지 않는다. 후보·이슈 큐 페이로드만 게시한다.

## 🔗 관련 문서

- [[wiki/Engineering/Infrastructure-and-DevOps/GitHub-Fine-Grained-PAT-Contents-Write-Probe.md]]
- [[wiki/Engineering/AI-Native-Engineering/Hugo-External-Link-New-Tab.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
