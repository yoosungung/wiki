---
id: roadmap-sync-unchecked-h2-gate
title: "ROADMAP sync: ## + 미완료 - [ ] 섹션만 enqueue"
status: canonical
owner: km
updated: "2026-10-14"
last_updated: "2026-10-14"
review_after: "2027-01-14"
sources:
  - schedule:pm-roadmap-sync
  - inbox/pm/2026-09-17-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-15-roadmap-sync-codingland-m4.md
  - inbox/pm/2026-09-07-pm-roadmap-sync-codingland.md
  - inbox/pm/2026-08-29-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-03-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-04-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-05-codingland-roadmap-sync-m4.md
  - inbox/pm/2026-09-06-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-08-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-09-codingland-roadmap-sync-m4.md
  - inbox/pm/2026-09-10-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-12-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-13-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-14-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-10-04-roadmap-sync-no-next.md
  - inbox/pm/2026-10-04-roadmap-next-enqueue.md
  - inbox/pm/2026-10-05-roadmap-sync.md
  - inbox/pm/2026-10-06-roadmap-sync.md
  - inbox/pm/2026-10-07-roadmap-sync.md
  - inbox/pm/2026-10-08-roadmap-sync.md
  - inbox/pm/2026-10-09-roadmap-sync.md
  - inbox/pm/2026-10-10-roadmap-sync.md
  - inbox/pm/2026-10-12-roadmap-sync.md
  - inbox/pm/2026-10-13-roadmap-sync.md
  - inbox/pm/2026-10-14-roadmap-sync.md
  - ticket:6beb03a9-b4cf-4096-995d-20b98ca918a9
  - ticket:012deff8-61cf-4270-86f7-de83b5d1f32b
  - ticket:10fe0055-84a9-47c1-9e2c-5ca3f638c51a
  - ticket:d13290fa-bf2f-4f41-ac2a-e5d9db243eea
  - ticket:51724bbd-8861-497d-b125-9b1e67ea2fd5
  - ticket:4c55a7df-66c0-4f40-a65e-468bbf438b8d
tags: ["Engineering", "AI-Native", "Roadmap", "Leantime", "Sync"]
type: "wiki"
---

# ROADMAP sync: ## + 미완료 `- [ ]` 섹션만 enqueue

`pm-roadmap-sync`는 `##` 섹션 중 **첫 미완료 `- [ ]` 체크리스트**만 티켓으로 만든다. `###` 하위·일반 `-` bullet·서술(“M0 Done”)만으로는 **no-op**(티켓 0).

## 문서 계약

```markdown
## 현재 마일스톤 이름
- [ ] 작업 A
- [ ] 작업 B
- [x] 완료된 항목

### 나중 마일스톤   # sync 대상 아님
- 그냥 bullet     # 무시
```

## 함정

- `## 마일스톤` 아래 `### M0…M4` + plain bullet만 있으면 sync가 영원히 0.
- 서술로만 “착수”를 적어도 Leantime 티켓은 안 생김 → current milestone을 `##` + `- [ ]`/`- [x]`로 바꾼다.
- Dedup: `<!-- roadmap:repo_id:slug -->`.
- `## 마일스톤` 아래 `### M3.1 — current` plain bullet은 sync 대상이 아님. 다음 체크리스트는 `##` + `- [ ]`가 생기기 전 no-op.
- leftover `type=milestone` New는 자식·pass-gate Done 후 위생 closeout — [[wiki/Engineering/AI-Native-Engineering/Orphan-Milestone-Close-After-Children-Done.md]].
- `### 나중` (plain H3 catalog) alone is **not** H2-checklist enqueue. After human asks to ticketize later-scope, create milestone+children with dedup markers; skip already-done markers even if ROADMAP checkbox still open (doc lag).

## Leantime Done ≠ ROADMAP 체크 완료 (idempotent)

- sync는 **ROADMAP.md의 `- [ ]`만** 보고 enqueue한다. Leantime 자식 티켓이 이미 Done이어도 ROADMAP 체크박스가 열려 있으면 해당 `##`는 **current로 남는다**.
- Dedup 마커(`<!-- roadmap:… -->`)가 있으면 **티켓을 다시 만들지 않는다**(idempotent skip). sync가 ROADMAP을 `- [x]`로 고쳐 쓰지 않는다.
- **Pass-gate / approved→next**는 incomplete `##`가 0이 될 때까지 deferred. 다음 `##`/`###` enqueue는 current 체크리스트가 문서상 닫힌 뒤에만.
- 운영: 마일스톤 티켓 재사용 + 자식 skip은 정상; “Done인데 sync가 또 current”는 버그가 아니라 **문서·보드 축 분리**다. 진행을 넘기려면 ROADMAP 체크를 사람이(또는 pass-gate 승인 후) 닫는다 — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]].
- **2026-10-06···10 uni-tutor:** `## 나중`에 LMS/LTI `- [ ]` 1개만 남아 current; milestone `f8d92c00` 재사용 + LMS marker `4aa8d43d` → enqueue skip / `created=0`, pass-gate deferred (checkbox open). crewrp incomplete 0 → freeze no-op (Phase 4 invent 금지; pass-gate `f9f2416a` already `done`).
- **2026-10-12:** crewrp current=`## Phase 4 — 소통 = Discord 계정 연동` → milestone `012deff8` + child `6beb03a9` (marker `roadmap:crewrp:discord-oauth-app-server-channel-keys-manual-e2e`); Phase 5/6 blocked. uni-tutor LMS/LTI still open checkbox + done marker `4aa8d43d` → `created=0` / doc lag; pass-gate deferred while any incomplete `##` remains. Discord E2E: [[wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md]].
- **2026-10-13:** crewrp current=`## Phase 5 — 소통 허브 + 홈 README` → milestone `10fe0055` + child `d13290fa` (`roadmap:crewrp:home-readme-comm-category-manual-e2e`); Phase 6 blocked. uni-tutor LMS/LTI still open checkbox + done marker `4aa8d43d` → `created=0` / doc lag. Phase 5 E2E: [[wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md]].
- **2026-10-14:** crewrp current=`## Phase 6 — 할 일·게시판 댓글` → milestone `51724bbd` + child `4c55a7df` (`roadmap:crewrp:todo-board-comment-crud-manual-e2e`); Phase 7+ blocked. uni-tutor: registry 있으나 pm membership 403 → skip enqueue. Pass-gate N/A while incomplete `##` remains; `tenant_cd` N/A for crewrp. Phase 6: [[wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Discord-OAuth-Manual-E2E.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Phase5-Home-Comm-Manual-E2E.md]]
- [[wiki/Engineering/Development-Environment/CrewRP-Phase6-Todo-Board-Comments.md]]
