---
id: inbox-candidate-2026-08-15-publication-safety
agent: candidate
ticket_id: 820
updated: 2026-08-15
status: inbox
sources:
  - ticket:820
  - wiki/Engineering/AI-Native-Engineering/Publication-Gate-Empty-Overwrite-Guard.md
---

# Publication-safety: remap/drop before ship

- Gate PASS is not content-safe: remap unique `name_ko`/alias people slugs, then drop org-as-person and SSoT-missing stance lines in the unpublished issue diff.
- Keep yaml↔wiki orphan at 0 by seeding a minimum wiki stub when Pass D adds people YAML.
- Diverged Pass stack ships by rebase onto `origin/main` (not ff-merge of curation into the stack). `http.extraheader` plus an embedded remote token can 401; one push with the tenant override in the URL is enough.
