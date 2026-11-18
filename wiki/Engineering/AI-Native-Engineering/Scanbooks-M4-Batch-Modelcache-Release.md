---
id: scanbooks-m4-batch-modelcache-release
title: "scanbooks M4: batch reorder · ModelCache · attribution · license gate"
status: canonical
owner: km
updated: "2026-11-19"
last_updated: "2026-11-19"
review_after: "2027-02-19"
sources:
  - inbox/scanbooks/2026-11-18-m4-attribution-privacy-notice.md
  - ticket:5c56d7ab-77d4-4459-8a67-6a0dbed4cdce
  - inbox/scanbooks/2026-11-18-m4-batch-reorder-delete.md
  - ticket:c5308fcf-b10b-48c7-aa76-d03e2863797f
  - inbox/scanbooks/2026-11-18-m4-modelcache-ondemand.md
  - ticket:5f79ae5a-0ecb-4c81-b8f3-ebf35ce3b4c6
  - inbox/scanbooks/2026-11-18-m4-release-license-checklist.md
  - ticket:dab69fd0-4d61-4252-9c66-ffcacd5ce214
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-empty1.md
  - ticket:d6076cca-10d7-4b39-964d-54c3fb3d44f3
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-empty1hold.md
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-empty2.md
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-empty2hold.md
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-empty3-approval.md
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-seal.md
  - inbox/pm/2026-11-18-pm-checkpoint-scanbooks-m4-under30.md
  - inbox/pm/2026-11-18-scanbooks-m4-attribution-intent-pass.md
  - inbox/pm/2026-11-18-scanbooks-m4-batch-intent-pass.md
  - inbox/pm/2026-11-18-scanbooks-m4-release-checklist-intent-pass.md
tags: ["Engineering", "scanbooks", "Mobile", "Release"]
type: wiki
---

# scanbooks M4: batch reorder · ModelCache · attribution · license gate

Builds on [[wiki/Engineering/AI-Native-Engineering/Scanbooks-M3-Pipeline-Ort-Temp-Smoke.md]]. `tenant_cd` N/A for mobile — Done = Intent + merge + test evidence.

## Durable M4 facts

- - Settings route + `AttributionPresentation` (iOS/Android): privacy body, DocTr/ORT/OpenCV credits, non-commercial notice, About `modelVersion`.
- - First-scan tip = privacy short + processing detail (UIUX §1.7); Camera ⋯ opens Settings.
- - FingerSeg final weights still pending — attribution scope excludes that row until selected (ROADMAP license table).
- - Continuous batch (UIUX §3.2): shutter stays on Camera; background `PipelineRunner`; badge `처리 중 N장` via `BatchScanPresentation`.
- - Session (UIUX §4.4): `SessionStore.reorderPages` / `deletePage` rewrites `pageIds` + `Page.index` and removes page dir; UI move / select-delete / 추가 스캔.
- - Pure helpers shared: `BatchScanPresentation`, `SessionPageOrder` (iOS/Android).
- - Evidence: Android SessionStoreTest+BatchScanPresentationTest · iOS SessionStoreTests+BatchScanPresentationTests · PR #20.
- - `models/manifest.json` `deploy`: `residentPreferred` (geo/seg/finger) · `onDemand` (illtr). Optional `downloadURL`/`checksumSha256`.
- - App `ModelCache.ensure` / `ensureResidentPreferred` → `OrtModelCatalog`; IllTr absent → ill passthrough (pipeline order intact).
- - Missing resident file + null URL → soft-skip (no launch crash until CDN/LFS).
- - `workLongEdgeMitigated=768` constant only; default remains 1024 (ARCHITECTURE §5.4).
- - `docs/RELEASE_CHECKLIST.md` + `ReleaseChecklistGate` (iOS/Android): internal distribution **pass**, commercial store **blocked** until DocTr written permission.
- - Open rows locked in tests: `doctr_commercial`, `fingerseg_final_weights` (manifest still `candidate_a_pending_weights`).
- - Closed for internal path: non-commercial DocTr · ORT/OpenCV notice · attribution UI · privacy notice · UX OSS reference-only.

## Milestone seal

- M4 empty 1/3→3/3 + Approval path ran via pm-checkpoint; milestone sealed after Intent passes on attribution · batch reorder/delete · ModelCache · release license checklist.
