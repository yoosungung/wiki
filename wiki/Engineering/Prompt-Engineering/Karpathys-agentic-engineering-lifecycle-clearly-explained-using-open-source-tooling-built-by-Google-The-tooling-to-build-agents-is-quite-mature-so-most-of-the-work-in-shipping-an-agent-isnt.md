---
title: "Karpathy's agentic engineering lifecycle, clearly explained

(using open-source tooling built by Google)

The tooling to build agents is quite mature, so most of the work in shipping an agent isn't…"
related_raw: ["[[raw/Karpathy's agentic engineering lifecycle, clearly explained

(using open-source tooling built by Google)

The tooling to build agents is quite mature, so most of the work in shipping an agent isn't….md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Karpathy's agentic engineering lifecycle, clearly explained

(using open-source tooling built by Google)

The tooling to build agents is quite mature, so most of the work in shipping an agent isn't…

Karpathy's agentic engineering lifecycle, clearly explained: (using open-source tooling built by Google) The tooling to build agents is quite mature, so most of the work in shipping an agent isn't writing the agent anymore. It's everything after, including scaffolding it, deploying it to a runtime, locking down its identity and network, evaluating it, and publishing it somewhere people can use. Each of those has traditionally lived in its own console, its own config, its own separate tool. Google's Agents CLI + skills implements procedures to condense the entire lifecycle into the coding agent itself, by prompting in plain English. A setup command injects the lifecycle skills, so a single coding agent can carry an idea from an empty folder to a governed, published enterprise asset. I mapped the full lifecycle in the diagram below. Here's what each stage does. > Setup installs the skills into any coding agent (Claude Code, Cursor, Codex, Antigravity) from one command. > Build scaffolds the agent and its deterministic tools from a prompt, then you run it locally in the playground. > Deploy pushes it onto Agent Runtime with Sessions and Memory Bank, so it holds state across runs. > Govern is the security stage, and Agents CLI drives all of it from prompts. It provisions a dedicated least-privilege identity, screens untrusted text for prompt injection through Model Armor, and confines the agent to an egress allow-list of hosts you approve. > Evaluate checks grounding and hallucination, and then optimizes the prompt while proving no regression. > Publish registers the agent into Gemini Enterprise for the whole org to use. Every stage requires just natural-language prompts. Link to agents CLI GitHub repo in the first comment! \_\_\_\_\_ Share this with your network if you found this insightful ♻️ Follow me ([Akshay Pachaar](https://in.linkedin.com/in/akshay-pachaar?trk=public_post-text)) for more insights and tutorials on AI and Machine Learning!

---
- **Source:** Unknown
