---
title: Light RAG
related_raw:
  - "[[wiki/RAG/Light RAG]]"
tags:
  - wiki
  - knowledge_and_memory
  - advanced_rag_&_knowledge_graph
  - graphrag_implementation
type: wiki
status: draft
last_updated: "2026-04-19"
---

1. 적재
	1. doc -> array of chunk
	2. chunk
		1. -(embedding)-> vector db
		2. -> key-value db
		3. -(llm)-> array of {subject, predicate, object}
	3. entities (subject, object)
		1. -(llm)-> name (중복제거), description (통합)
		2. description -(embedding)-> vector db
		3. name (중복제거) -> kg db (knowledge graph db)
	4. relations (predicate)
		1. -(llm)-> name (중복제거), description (통합)
		2. description -(embedding)-> vector db
		3. name (중복제거) -> kg db
	5. kg db (local) -(summary)-> kg db (summary)
2. 쿼리
	1. message -(llm)-> keywords
	2. keywords -(embedding -> vector db)-> top k of {entities, relations}
		1. entities
			1. -(kg db)-> array {object, subject}
			2. {object, subject} -(kg db)-> predicate
		2. relations -(kg db)-> {subject, predicate, object}
	3. step 2 반복 kg db (summary)
	4. entities.description + relations.description + chunk.text -(llm)-> response