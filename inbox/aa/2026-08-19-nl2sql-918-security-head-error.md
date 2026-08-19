---
id: inbox-aa-nl2sql-918-security-head-error
agent: aa
ticket_id: 918
updated: 2026-08-19
status: inbox
sources:
  - ticket:918
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - https://aicodingguild.com/blog/api-error-handling-what-to-return-and-what-to-swallow
---

# nl2sql #918 list_fs head_error — AA security gate

- `.factory/quality.yaml`에 `security.command` 없음 → mechanical skip + scoped manual (auth/secret/transport).
- Delta(`443185d` / merge `85cba02`): corrupt JSON에 `head_error=str(exc)` + warning; `console_principal` 유지; dotfile 필터 유지.
- Residual (Low, not gate-fail): `MetadataRepoError` 드물게 abs path 포함 가능 — console-auth 호출자만 수신; 일반 경로는 JSON parse/rel-path.
- Unit: `test_ls_corrupt_json_sets_head_error` + `test_ls_includes_kind_and_head` pass.
