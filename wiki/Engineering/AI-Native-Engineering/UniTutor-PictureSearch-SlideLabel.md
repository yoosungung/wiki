---
id: unitutor-picturesearch-slidelabel
title: "UniTutor PictureSearch Option A (slideLabel/concept → seek)"
status: canonical
owner: km
updated: "2026-10-05"
review_after: "2027-01-05"
sources:
  - inbox/pm/2026-10-04-unitutor-slide-visual-search-slice-a.md
  - inbox/pm/2026-10-04-unitutor-picture-search-intent-pass.md
  - inbox/pm/2026-10-04-unitutor-picture-search-done.md
  - inbox/uni-tutor/2026-10-04-unitutor-picture-search-slideLabel.md
  - inbox/qa/2026-10-04-unitutor-picture-search-qa-pass.md
  - inbox/aa/2026-10-04-unitutor-picture-search-security-pass.md
  - inbox/ta/2026-10-04-unitutor-picture-search-prod-pass.md
  - ticket:d4a9f487-7325-4ecc-b9b4-3dee165a425b
  - https://github.com/yoosungung/UniTutorAI/pull/26
tags: ["Engineering", "AI-Native", "UniTutor", "PictureSearch"]
type: "wiki"
---

# UniTutor PictureSearch Option A (slideLabel/concept → seek)

## Slice

- Static `SourceSpan.slideLabel` / `concept` substring search → existing `CitationSelected` / `startSec` seek.
- Entry: `frontend/src/lib/pictureSearch.ts`, `components/canvas/PictureSearch.tsx`.
- Out-of-scope: vision/embedding search, Editor/Roommate MVP, ARCHITECTURE schema change.
- PRODUCT §7 image/vision search remains later.

## Evidence (merge `f39e3fe`, PR #26)

- `test:` frontend npm test 110 passed; CI backend+frontend green.
- QA/TA smoke: Deploy 37164460300; `api.tutor.askwho.net/health` 200; Pages 200; Playwright seek `JP7ITIXGpHk?start=341`.
- AA: FE-only, no new auth/API surface; mechanical SAST N/A (no `.factory/quality.yaml` security.command).
- UniTutor prod = Cloudflare push→main (not k8s tenant_cd). Done after intent+test+qa+aa+prod.

## Related

- [[wiki/Engineering/AI-Native-Engineering/UniTutor-TutorTurn-SSE-Inference.md]]
- [[wiki/Engineering/AI-Native-Engineering/UniTutor-Editor-Roommate-Canvas.md]]
- [[wiki/Engineering/Infrastructure-and-DevOps/UniTutor-Cloudflare-Deploy.md]]
