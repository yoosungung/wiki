---
id: inbox-pm-unitutor-editor-roommate-intent-pass
agent: pm
ticket_id: 66ac47e7-d156-4701-9cc7-1bc01e537550
updated: 2026-10-05
status: inbox
sources:
  - ticket:66ac47e7-d156-4701-9cc7-1bc01e537550
  - https://github.com/yoosungung/UniTutorAI/pull/30
  - inbox/uni-tutor/2026-10-05-editor-roommate-same-canvas.md
  - inbox/pm/2026-10-05-unitutor-editor-roommate.md
---

# UniTutor Editor/Roommate MVP — Intent pass

- Same-canvas Tutor pane tabs (`LaterModePane`); no new route / TutorTurn fields.
- Editor: static `coachEditorDraft` → one coaching question on current `sourceSpanId`.
- Roommate: lecture hit → `in_lecture`+citations; else `out_of_scope`+empty citations.
- PictureSearch seek path unchanged; vision/embedding search still PRODUCT §7 later.
- Merged: https://github.com/yoosungung/UniTutorAI/pull/30 (`cc3b4c961181d23a5be472588cc40af709f7a49d`).
