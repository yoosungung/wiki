---
id: roadmap-sync-unchecked-h2-gate
title: "ROADMAP sync: ## + 미완료 - [ ] 섹션만 enqueue"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - schedule:pm-roadmap-sync
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

## 🔗 관련 문서

- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
- [[wiki/Engineering/AI-Native-Engineering/Schedule-Outcome-Requires-Active-Ticket.md]]
