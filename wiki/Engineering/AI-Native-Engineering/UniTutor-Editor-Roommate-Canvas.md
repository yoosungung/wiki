---
id: unitutor-editor-roommate-canvas
title: "UniTutor Editor/Roommate: same-canvas Tutor pane tabs"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-05"
sources:
  - inbox/uni-tutor/2026-10-05-editor-roommate-same-canvas.md
  - inbox/pm/2026-10-05-unitutor-editor-roommate.md
  - inbox/pm/2026-10-05-unitutor-editor-roommate-intent-pass.md
  - ticket:66ac47e7-d156-4701-9cc7-1bc01e537550
  - https://github.com/yoosungung/UniTutorAI/pull/30
tags: ["Engineering", "AI-Native", "UniTutor", "Editor", "Roommate"]
type: "wiki"
---

# UniTutor Editor/Roommate: same-canvas Tutor pane tabs

## Contract

- Editor/Roommate are **Tutor pane mode tabs** (`LaterModePane`), not separate routes. Player + talk stay one session.
- Editor: static `coachEditorDraft` → one coaching question on current `sourceSpanId`.
- Roommate: lecture hit → `in_lecture`+citations; off-lecture → existing `TutorTurn.scope=out_of_scope` + empty citations. No schema patch.
- PictureSearch seek path unchanged. Vision/embedding slide search remains PRODUCT §7 later.

## Roadmap note

- `## 나중` bundled visual-search + Editor + Roommate; PictureSearch slice already done (`d4a9f487`). Remainder ticket `66ac47e7`.
- Splitting Roommate off the study canvas would violate ARCHITECTURE session contract unless Eric-approved schema change.

## Evidence

- Intent merge PR #30 (`cc3b4c9`).
