---
title: "An agent approved a loan in January."
related_raw: ["[[raw/An agent approved a loan in January..md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# An agent approved a loan in January.

An agent approved a loan in January. In August the audit question is why, and the log has the outcome but not the reasoning behind it. Semantica records each decision as a graph node with its rationale, linked to the decisions that caused it and the entities it touched. On main, entries chain to each other, so a deleted row shows up. 1.9k stars, MIT. [#KnowledgeGraph](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fknowledgegraph&trk=public_post-text) [#AIGovernance](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Faigovernance&trk=public_post-text) [#AIAgents](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Faiagents&trk=public_post-text) [#Provenance](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Fprovenance&trk=public_post-text) [#AIEngineering](https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2Fhashtag%2Faiengineering&trk=public_post-text)

I have worked on lineage and retention long before the current AI cycle, and the same lesson applies here: an audit trail is only useful if it captures the inputs, policy version, tool calls and approval that existed when the decision was made. A graph can make the chain visible and tamper-evident. It still needs to distinguish contemporaneous evidence from a rationale reconstructed by the model after the fact, or the neatest node in the graph may be the least reliable one.

Decision provenance is the missing half of agent governance, agreed. One caveat from testing memory based agents though: the graph records the rationale the agent stated, and that rationale reads perfectly sound even when the context behind it was manipulated. In my own tests two ordinary chat messages were enough to plant a false fact in a Mem0 memory and have it steer later behaviour. Does a Semantica node also pin the provenance of its inputs, so you can trace back to the retrieved chunks or memory entries that produced the reasoning?

Storing the outcome without the reasoning state is the standard failure mode, and it only surfaces when someone asks a question the log was never designed to answer. Point-in-time reconstruction requires knowing what facts were in scope, which rules fired, and whether any upstream source had been revised before the decision landed. The append-only chain addresses the deletion problem directly. The open question is how SHACL constraint violations are surfaced during ingestion when a new source contradicts an entity that earlier decisions already relied on.

---
- **Source:** Unknown
