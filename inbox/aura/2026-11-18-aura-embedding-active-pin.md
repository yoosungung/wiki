---
id: inbox-aura-embedding-active-pin
agent: aura
ticket_id: 827b233f-0d69-4ed6-934f-5201043aeeb2
updated: 2026-11-18
status: inbox
sources:
  - ticket:827b233f-0d69-4ed6-934f-5201043aeeb2
  - wiki/Models/Optimization-and-Serving/SGLang-gemma4-llm-serving-cluster-ops.md
  - https://huggingface.co/BAAI/bge-m3
---

# Aura M1 활성 AURA_EMBEDDING_* 핀

- 생산 핀: `AURA_EMBEDDING_MODEL=BAAI/bge-m3` · `version=1`(운영 세대) · `dims=1024` · `model_key=BAAI/bge-m3:1`
- 근거: 클러스터 TEI 이름 `bge-m3-tei` + HF dense dims=1024 (발명 금지)
- SoR: aura `deploy/docs/memory-embedding-active.md` · 정적 `check-memory-embedding-active.sh`
- TTL(14d/24mo/12mo)은 `memory-ttl-policy.md` 유지 — 이 슬라이스에서 재고정하지 않음
