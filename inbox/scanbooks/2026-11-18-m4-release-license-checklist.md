---
id: inbox-scanbooks-m4-release-license-checklist
agent: scanbooks
ticket_id: dab69fd0-4d61-4252-9c66-ffcacd5ce214
updated: 2026-11-18
status: inbox
sources:
  - ticket:dab69fd0-4d61-4252-9c66-ffcacd5ce214
  - https://github.com/yoosungung/scanbooks/pull/23
---

# scanbooks M4: release license checklist gate

- `docs/RELEASE_CHECKLIST.md` + `ReleaseChecklistGate` (iOS/Android): internal distribution **pass**, commercial store **blocked** until DocTr written permission.
- Open rows locked in tests: `doctr_commercial`, `fingerseg_final_weights` (manifest still `candidate_a_pending_weights`).
- Closed for internal path: non-commercial DocTr · ORT/OpenCV notice · attribution UI · privacy notice · UX OSS reference-only.
