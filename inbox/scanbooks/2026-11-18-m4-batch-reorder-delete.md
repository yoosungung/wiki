---
id: inbox-scanbooks-m4-batch-reorder-delete
agent: scanbooks
ticket_id: c5308fcf-b10b-48c7-aa76-d03e2863797f
updated: 2026-11-18
status: inbox
sources:
  - ticket:c5308fcf-b10b-48c7-aa76-d03e2863797f
  - https://github.com/yoosungung/scanbooks/pull/20
---

# scanbooks M4: continuous batch + session reorder/delete

- Continuous batch (UIUX §3.2): shutter stays on Camera; background `PipelineRunner`; badge `처리 중 N장` via `BatchScanPresentation`.
- Session (UIUX §4.4): `SessionStore.reorderPages` / `deletePage` rewrites `pageIds` + `Page.index` and removes page dir; UI move / select-delete / 추가 스캔.
- Pure helpers shared: `BatchScanPresentation`, `SessionPageOrder` (iOS/Android).
- Evidence: Android SessionStoreTest+BatchScanPresentationTest · iOS SessionStoreTests+BatchScanPresentationTests · PR #20.
