---
title: "The distributed platform that powered Kimi K3's RL training!

AgentENV is the infrastructure that powered agentic RL training for Kimi K3 - running thousands of isolated sandboxes simultaneously…"
related_raw: ["[[raw/The distributed platform that powered Kimi K3's RL training!

AgentENV is the infrastructure that powered agentic RL training for Kimi K3 - running thousands of isolated sandboxes simultaneously….md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# The distributed platform that powered Kimi K3's RL training!

AgentENV is the infrastructure that powered agentic RL training for Kimi K3 - running thousands of isolated sandboxes simultaneously…

The distributed platform that powered Kimi K3's RL training! AgentENV is the infrastructure that powered agentic RL training for Kimi K3 - running thousands of isolated sandboxes simultaneously, each forkable, snapshotable, and resumable in milliseconds. Training agents with RL means running the same task across thousands of parallel environments. Each needs its own isolated sandbox where the agent can write code, run shell commands, and interact with the filesystem. Docker is too slow to start. Full VMs are too heavy. And at training scale, cloud sandbox costs compound fast. AgentENV uses Firecracker microVMs. Environments boot or resume in under 50ms and pause in under 100ms. When an agent finishes its turn and waits for the next update, the environment pauses and returns its memory to the host. When work arrives again, it resumes instantly from exactly where it left off. The fork capability is what makes parallel RL training practical. Instead of booting thousands of fresh VMs from the same base state, AgentENV snapshots one running environment and forks it into multiple independent sandboxes in under 100ms. Each fork is fully isolated. Agents try different approaches simultaneously without interfering with each other. Snapshots happen incrementally, completing in under 100ms even under heavy disk modification. They persist to S3-compatible object storage so no state is lost if a machine goes down. Local disk acts as a bounded cache, so images can exceed disk capacity without pre-warming every host. AgentENV also exposes an E2B-compatible HTTP API. If your agent code already uses the E2B SDK, point one environment variable at your AgentENV server and your existing code works without any changes. Key capabilities: • Firecracker microVM environments: boot and resume in under 50ms • Fork a running environment into multiple independent sandboxes in under 100ms • Incremental snapshots to S3-compatible storage in under 100ms • Memory ballooning returns idle guest memory to the host • Images can exceed disk capacity via overlaybd with on-demand loading • E2B-compatible HTTP API - drop-in replacement with no code changes • Distributed across machines via Kubernetes or Docker Compose I've shared the link in the replies!

---
- **Source:** Unknown
