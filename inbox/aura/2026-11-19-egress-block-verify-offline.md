---
id: inbox-aura-egress-block-verify-offline
agent: aura
ticket_id: eba42b9f-3f94-4519-acfe-5697307b6785
updated: 2026-11-19
status: inbox
sources:
  - ticket:eba42b9f-3f94-4519-acfe-5697307b6785
  - https://github.com/yoosungung/aura/pull/42
  - https://kubernetes.io/docs/concepts/services-networking/network-policies/
---

# Aura M3: Egress 차단 오프라인 검증

- V3.3 스모크 = `deploy/k8s/sandbox-egress/` NetworkPolicy deny-default allowlist + RuntimeClass 매니페스트 + `check-egress-block-verify.sh` (클러스터 불필요).
- Vanilla NP는 MCP HTTPS FQDN을 열 수 없음 → 앱 `egress-allowlist.js` + (문서) `aura-mcp-proxy` / Cilium toFQDNs.
- 비허용 증거: `egress_denied` / simulator DENY (provider LLM·metadata·미등록 MCP·PG primary).
- Live CNI 프로브·LLM Gateway 본구현은 Non-goal (`AURA_EGRESS_LIVE=1` 선택).
