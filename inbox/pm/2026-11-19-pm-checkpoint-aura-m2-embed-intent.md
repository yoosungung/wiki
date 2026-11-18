---
id: inbox-pm-aura-m2-embed-intent
agent: pm
ticket_id: fdee9181-52f2-4678-810c-cecf67fc3917
updated: 2026-11-19
status: inbox
sources:
  - ticket:fdee9181-52f2-4678-810c-cecf67fc3917
  - https://github.com/yoosungung/aura/pull/26
---

# Aura M2 embed Function MQT — Intent pass

- short_term → skipped_short_term (앱 가드, PG/set_config 미시도); episodic/long_term/semantic → withTenantTx + active model_key stub
- BM25 적격은 store content_tsv; HNSW 경로 소유는 embed (실 halfvec INSERT/TEI = Non-goal)
- 게이트: check-memory-embed.sh + handler.selftest.js; store/capture regression 유지
- PR#26 MERGED (3e40177); head feature/fdee9181-embed-function-mqt 삭제
- 다음 M2: recall RPC (25b46548) minReplicas>=2 · Core queue-group · MQT 없음
