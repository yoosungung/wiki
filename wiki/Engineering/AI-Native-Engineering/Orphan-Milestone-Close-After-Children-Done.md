---
id: orphan-milestone-close-after-children-done
title: "자식·pass-gate가 닫히면 남은 milestone을 Done한다"
status: canonical
owner: km
updated: "2026-08-13"
last_updated: "2026-08-13"
review_after: "2026-11-13"
sources:
  - ticket:540
tags: ["Engineering", "AI-Native", "Roadmap", "Leantime", "PM"]
type: "wiki"
---

# 자식·pass-gate가 닫히면 남은 milestone을 Done한다

`create_milestone`은 `type=milestone` 티켓을 **New + 빈 assignee**로 남길 수 있다. 부모 작업·pass-gate·다음 마일스톤이 이미 Done인데 보드에 New milestone만 남아 있으면 **위생 closeout**(assignee=pm, Done — Archived 아님).

`##` 아래 `### M3.1 — current` **plain bullet**만 있으면 everyday sync가 다음 체크리스트를 만들지 않는다. H2 `- [ ]`가 생기기 전에는 enqueue no-op — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md]].

pass-gate 마커가 이미 `m3-current` Done이면 `m3-done` 중복을 만들지 않는다 — [[wiki/Engineering/AI-Native-Engineering/Roadmap-Pass-Gate-Human-Approval.md]].

## 관련

- [[wiki/Engineering/AI-Native-Engineering/Parent-Done-Requires-Closed-Subtasks.md]]
- [[wiki/Engineering/AI-Native-Engineering/FS-Blocked-By-Vs-Parent-Link.md]]
