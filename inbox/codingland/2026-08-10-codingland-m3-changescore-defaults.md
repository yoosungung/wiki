---
id: inbox-codingland-m3-changescore-defaults
agent: codingland
ticket_id: 458
updated: 2026-08-10
status: inbox
sources:
  - ticket:458
  - https://doi.org/10.48550/arxiv.2602.20206
  - https://www.oliver-huang.com/static/uploads/papers/productive_friction.pdf
---

# codingland M3 ChangeScore experimental defaults

- M3 core: `computeChangeScore` severity = mean(entropy,coupling,criticality); sessionLoad≥0.7 → −0.25, ≥0.4 → −0.10; tier none<0.3 / light<0.6 / else full.
- `bypassAllowed` = criticality<0.7 or sessionLoad≥0.5 — never attempt===3 (ARCHITECTURE §1.9).
- Adaptive friction / teach-back aligned with epistemic-debt Explanation Gate literature (arxiv 2602.20206); productive friction design space (Huang et al.).
- Weights remain ROADMAP undecided until post-M3 experiment freeze.
