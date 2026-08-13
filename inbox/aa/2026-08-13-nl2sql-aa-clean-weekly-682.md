---
id: inbox-aa-nl2sql-aa-clean-weekly-682
agent: aa
ticket_id: 682
updated: 2026-08-13
status: inbox
sources:
  - ticket:682
  - ticket:684
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://homepages.dcc.ufmg.br/~figueiredo/publications/icsme2024preprint.pdf
---

# nl2sql aa-clean-weekly manual (#682)

- Mechanical `clean_code.command` (ruff+mypy+pytest) green at sha `7f519f2` — aligns with Quality-Yaml-Clean-Code-CI-Align.
- Prior High/Med #414–#417 Done and verified fixed (`repo_list_failed` Issue path; `_tool_result_payload`; `_push_and_notify_sync`; `_to_sse` helpers).
- New Med #684: `obj.god` on `agent/tool_payload.py` (SSE stash + LLM slim budgets + JSON sanitize agglomeration).
- Empirical note: smell agglomerations raise change intensity — prefer splitting interacting concerns over isolated nits.
