---
id: inbox-pm-2026-11-15-roadmap-sync
agent: pm
ticket_id: null
updated: 2026-11-15
status: inbox
sources:
  - schedule:pm-roadmap-sync
  - wiki/Engineering/AI-Native-Engineering/Roadmap-Sync-Unchecked-H2-Gate.md
  - .cursor/roadmap-registry.json
---

# ROADMAP sync 2026-11-15

- Registry repos: crewrp · aura · uni-semantic. factory-mcp absent → REST+session.cookie. Ticketless → no orphan Outcome comment.
- **crewrp:** incomplete `##` 0; passed=`## Phase 6`; Next `###` resolve fail (`### S7-*`에 `\bM\d+` 없음) → `no next ###` / invent 금지; `created=0`.
- **aura:** H2 checkbox 0 + no all-`[x]` passed section → skip `no passed section`; tickets=0.
- **uni-semantic:** current=`## Phase 4` (open MCP `- [ ]`); milestone `ba31c9e8` `waiting_for_approval` 유지(비강등); child marker `<!-- roadmap:uni-semantic:ir-기반-mcp-연동-sql-mcp-nl2sql-에이전트가-단일-스키마로-조회 -->` on done `d15d16f2` → dedup `created=0`; pass-gate deferred while checkbox open (doc lag / cancelled MCP).
- `tenant_cd` N/A for this sync set. git-ship N/A (no Review-ready code).
