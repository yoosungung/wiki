---
id: inbox-aa-2026-11-02-aa-clean-weekly
agent: aa
ticket_id: none
updated: 2026-11-02
status: inbox
sources:
  - schedule:aa-clean-weekly
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/AI-Native-Engineering/Quality-Yaml-Clean-Code-CI-Align.md
---

# aa-clean-weekly 2026-11-02

레지스트리 4 repo 전부 `clean_code:` 없음 → skip. High/Med=0. NF New 없음. prod 게이트 아님.

## Sync (tenant-repo-sync)

| repo_id | sha | quality.yaml | clean_code |
| :--- | :--- | :--- | :--- |
| sw-factory | `8e6f8af17dfc68482c8ce1cf5c0e9b10f6804242` | 없음 | skip (no `.factory/quality.yaml`) |
| crewrp | `47f03403a7ebb86925b4be99a35213ff074fd64d` | 없음 | skip |
| sql-mcp | `37da5744352979d2e179513e367c0ec737817cb9` | 없음 | skip |
| rhwp_batch | `642974c32716882fd96b4b5d3d74ab5fdb5fdec8` | 없음 | skip |

전부 dirty 아님, default branch ff-only 이미 up to date. mechanical command 미기동 → `nf-progress:` N/A.

## Discover / heuristic

- 레지스트리 변경: 이전 주 `sw-factory`/`crewrp`/`uni-tutor` → 이번 주 `sw-factory`/`crewrp`/`sql-mcp`/`rhwp_batch`. `uni-tutor` checkout은 워크스페이스에 남아 있으나 registry 밖.
- `nl2sql` `.factory/quality.yaml` `clean_code.command`(ruff+mypy+pytest) 는 registry 밖 → 범위 외. CI 3단 정합은 canonical `Quality-Yaml-Clean-Code-CI-Align.md`.
- factory-mcp `list_projects` 4건(registry와 동일). open/assignee=me/clean-code 검색 모두 0. Active 없음 → orphan Outcome 금지.
- `tenant-cd-registry.json` 부재 → feature Done 게이트 해당 없음.
- Cursor `factory` namespace 미노출. factory-mcp `FactoryClient`(session cookie REST)로 읽기만.

## Tickets

no High/Med
