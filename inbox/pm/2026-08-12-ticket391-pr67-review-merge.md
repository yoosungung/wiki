---
id: inbox-pm-ticket391-pr67-review-merge
agent: pm
ticket_id: 391
updated: 2026-08-12
status: inbox
sources:
  - ticket:391
  - https://github.com/yoosungung/nl2sql/pull/67
---

# #391 PR #67 review → merge → Deploying Test

- SoT tip `test-754707c`: #66 insufficient; residual timeout + Infinity BadRequest resurfaced.
- Fix: wrap_model_call message history / tool_calls.args sanitize + numpy-like scalars.
- CI green; local ruff/mypy + model-message sanitize tests pass.
- Next: TA tip roll + AC3 local008,local022 (empty SQL=0 · pass_rate>0).
