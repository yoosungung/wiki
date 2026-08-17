---
id: inbox-qa-nl2sql-opik-weekly-tmp-spider2
agent: qa
ticket_id: 924
updated: 2026-08-17
status: inbox
sources:
  - ticket:924
  - wiki miss: wiki/Agents/Evaluations (no nl2sql weekly opik ops page)
---

# nl2sql spider2-opik weekly — ephemeral clone needs .tmp-spider2

- `tenant-repo-sync` depth-1 clone of nl2sql does **not** include gitignored `spider2-eval/.tmp-spider2` (Spider2-Lite jsonl assets).
- First `spider2-opik weekly` check hard-fails: `missing .../.tmp-spider2/Spider2/spider2-lite/spider2-lite.jsonl`.
- Fix used 2026-08-17: symlink `/tmp/tenant-repos/nl2sql/spider2-eval/.tmp-spider2` → workspace `/workspace/repo/spider2-eval/.tmp-spider2` (or set `SPIDER2_TMP_DIR` to a populated tree), then restart weekly.
- After restart: check → gold-sql smoke (`weekly-gold-sql-smoke`) → agent smoke (`weekly-agent-smoke`) all EXIT:0; `spider2_exec_match`/`pass_rate` 1.0 on local008,local022; `nf-progress.json` phase=done.
