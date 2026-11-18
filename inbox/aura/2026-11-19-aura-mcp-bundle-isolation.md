---
id: inbox-aura-mcp-bundle-isolation
agent: aura
ticket_id: 220f8247-4c19-45de-859c-3130531b0b33
updated: 2026-11-19
status: inbox
sources:
  - ticket:220f8247-4c19-45de-859c-3130531b0b33
  - https://bex.co/blog/2026/07/09/kata-containers-vs-gvisor-runtimeclass-selection
  - https://northflank.com/blog/kata-containers-vs-gvisor
---

# Aura MCP·번들 격리 정책 (M3)

- M3 기본 RuntimeClass = **gVisor `runsc`** (`gvisor`); 고위험 티어 = **Kata** (`kata`). Fission scale-to-zero·콜드 민감 때문에 gVisor 기본.
- Egress = **deny-default**; allowlist = NATS · CNPG Pooler · LLM Gateway · `aura-content` · 등록 MCP 호스트 · 클러스터 DNS. Barman `aura-pg`는 테넌트 샌드박스 allowlist에 넣지 않음.
- 플랫폼 서명 번들도 Egress NP는 커스텀과 **동일**. 미서명 커스텀을 `runc`로 돌리면 계약 위반.
- 정책 정본: aura `deploy/docs/mcp-bundle-isolation.md` · 정적 게이트 `check-mcp-bundle-isolation.sh`. 라이브 NP/실측은 후속.
