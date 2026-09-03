---
id: roadmap-sync-unchecked-h2-gate
title: "ROADMAP sync: ## + 미완료 - [ ] 섹션만 enqueue"
status: canonical
owner: km
updated: "2026-09-04"
last_updated: "2026-09-04"
review_after: "2026-11-29"
sources:
  - schedule:pm-roadmap-sync
  - inbox/pm/2026-08-29-codingland-roadmap-sync-m4-idempotent.md
  - inbox/pm/2026-09-03-codingland-roadmap-sync-m4-idempotent.md
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

## Leantime Done ≠ ROADMAP 체크 완료 (idempotent)

- sync는 **ROADMAP.md의 `- [ ]`만** 보고 enqueue한다. Leantime 자식 티켓이 이미 Done이어도 ROADMAP 체크박스가 열려 있으면 해당 `##`는 **current로 남는다**.
- Dedup 마커(`<!-- roadmap:… -->`)가 있으면 **티켓을 다시 만들지 않는다**(idempotent skip). sync가 ROADMAP을 `- [x]`로 고쳐 쓰지 않는다.
- **Pass-gate / approved→next**는 incomplete `##`가 0이 될 때까지 deferred. 다음 `##`/`###` enqueue는 current 체크리스트가 문서상 닫힌 뒤에만.
- 운영: 마일스톤 티켓 재사용 + 자식 skip은 정상; “Done인데 sync가 또 current”는 버그가 아니라 **문서·보드 축 분리**다. 진행을 넘기려면 ROADMAP 체크를 사람이(또는 pass-gate 승인 후) 닫는다 — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]].

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
