---
title: "Memory"
related_raw: ["[[wiki/Agents/Memory-and-Cognition/Memory.md]]"]
tags: ['wiki', 'knowledge_and_memory', 'advanced_rag_&_knowledge_graph', 'agent_memory_and_cognition']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

1. 단기기억 (20~30초)
	1. 작업기억
		1. 구현 : state
2. 장기기억 (+조회횟수 / 최근조회일시, -미사용 삭제)
	1. 구현 : (graph + vector) db
	2. 일화기억 : Thread_Id, User_Id, title (+vector)
		1. 대화 추가
	3. 의미기억 : Graph DB (+vector)
		1. 조회결과 -> 단기가억 -> 누적 갱신 (meta 관리)
	4. 절차기억 : Graph (GIST+vector)
		1. 점화기억 : idea.description (+vector)
		2. 갱신 가능
3. Vector - Graph DB
	1. 기능
		1. Clean node
		2. Enhance data with node
		3. Merge node