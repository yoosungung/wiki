---
id: inbox-sw-factory-ticket50-parent-done-gate-ship-blocker
agent: sw-factory
ticket_id: 50
updated: 2026-07-31
status: inbox
sources:
  - ticket:50
  - https://support.leantime.io/en/article/subtasking-with-leantime-6l9nmw/
  - https://docs.github.com/rest/git/refs#create-a-reference
---

# #50 parent-Done gate ready; sw-factory ship blocked

- Applied equivalent of ticket patch on `feature/50-pm-parent-done-subtask-gate` (commit `6dbad24`): `pm-workflow` Parent Done hard gate + SKILL/pitfalls/ticket-ops + `test_pm_parent_done_requires_closed_subtasks`.
- Local verify: `cd deploy/k8s/scripts && python -m pytest test_sdlc_gates.py test_persona_bundle.py::test_build_pm_bundle_includes_leantime_pm_skill -q` → 7 passed.
- Developer Pod `GH_TOKEN` (yoosungung) still cannot `git push` / `POST /git/refs` on `yoosungung/sw-factory` (HTTP 403 fine-grained Contents Write missing) despite REST `permissions.push=true`.
