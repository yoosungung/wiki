---
id: inbox-pm-scanbooks-m2-done-roadmap-lag-blocks-m3
agent: pm
ticket_id: d4325e10-c8e2-4974-9df9-5c8bdbc92b44
updated: 2026-11-17
status: inbox
sources:
  - ticket:d4325e10-c8e2-4974-9df9-5c8bdbc92b44
  - https://github.com/yoosungung/scanbooks/blob/main/ROADMAP.md
---

# scanbooks M2 factory done ≠ M3 enqueue

- Factory M2 milestone `d4325e10` + children all `done`; project has no M3 / pass-gate ticket yet.
- Blocker: `ROADMAP.md` `## M2` still has open `- [ ]` (UI/camera/ScanSession/stub/vFlat). Sync current = first incomplete H2 → stays on M2 (`created=0` doc lag).
- After all M2 boxes `[x]`, still need human pass-gate + `<!-- roadmap-pass:approved -->` before M3 parent enqueue — do not invent M3 while H2 open.
