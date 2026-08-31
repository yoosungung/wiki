---
id: inbox-candidate-2026-08-31-publication-safety
agent: candidate
ticket_id: null
updated: 2026-08-31
status: inbox
sources:
  - schedule:publication-safety-03:00-KST
  - repo:berryking404/candidate.win@81a1401
---

# Publication-safety 03:00 KST — stance link hygiene

- Gate `publication_gate.py --base origin/main` checks only zero-stance ongoing issues; full unpublished diff still needs manual /people link audit before push.
- Pending agent stance batches often invent org/institution slugs and alias variants (`lee-jae-myung`, `ahn-cheol-soo`); remap to SSoT or de-link.
- Diverged main (local issue passes vs remote people curation) should rebase onto `origin/main` before publication push.
