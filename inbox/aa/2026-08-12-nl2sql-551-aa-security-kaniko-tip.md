---
id: inbox-aa-nl2sql-551-aa-security-kaniko-tip
agent: aa
ticket_id: 551
updated: 2026-08-12
status: inbox
sources:
  - ticket:551
  - wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md
  - wiki/Engineering/Infrastructure-and-DevOps/K8s-Secret-vs-ConfigMap-Deploy-Hardening.md
  - wiki/Engineering/Infrastructure-and-DevOps/Test-Overlay-vs-Release-Package-Deploy-Paths.md
  - https://github.com/advisories/GHSA-6rxq-q92g-4rmf
---

# nl2sql #551 AA security — Kaniko tip scoped pass

- `.factory/quality.yaml` has no `security.command` → mechanical skip; scoped manual review only (do not invent SAST).
- Delta (#63 / merge `52d0b76`): Kaniko Jobs + tip script; GHCR creds via Secret `nl2sql-ghcr-build` (github-token init readOnly; config.json → `/kaniko/.docker/`); no product auth/Host surface change.
- Live tip: backend `ghcr.io/yoosungung/nl2sql-backend:test-52d0b76`; Jobs Complete; `/api/ready` 200; unauth `/api/chat` + `/api/conversations` → 401.
- Executor pin `gcr.io/kaniko-project/executor:v1.23.2` outside CVE-2026-28406 range (1.25.4–1.25.9); context `dir://` not tar extract. Upstream archived — Chainguard/self-build remains tech debt (documented in SETUP).
- Residual (pre-existing, not #551 delta): ConfigMap `nl2sql-config` key `OPENAI_API_KEY` (wiki Forbidden pattern); follow-up NF/scrubber, not this gate fail.
