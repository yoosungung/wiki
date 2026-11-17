---
id: inbox-pm-scanbooks-m3-intent-pass-option2
agent: pm
ticket_id: de05921c-ffdf-41ef-88d7-2053f9a7dd9c
updated: 2026-11-18
status: inbox
sources:
  - ticket:de05921c-ffdf-41ef-88d7-2053f9a7dd9c
  - ticket:377c50be-63b7-4293-927b-8886b69c5ce3
  - https://github.com/yoosungung/scanbooks/pull/18
---

# scanbooks M3 Intent pass — option 2 temp device smoke

- Eric approved option 2 (2026-11-17): sim/emu + fixture 3 pages → done+PDF as temporary M3 gate; physical mid-range USB deferred.
- Intent pass with explicit `drift: sim/emu temporary evidence`; PR #18 merge `3b929e04`; no GitHub workflows/checks on scanbooks — local xcodebuild/gradle evidence accepted.
- PassthroughStageBackend fixture tests do not re-prove live ORT (covered by earlier M3 PRs #15–#17).
