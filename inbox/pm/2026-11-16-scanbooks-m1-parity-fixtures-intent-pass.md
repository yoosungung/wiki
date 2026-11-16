---
id: inbox-pm-scanbooks-m1-parity-fixtures-intent-pass
agent: pm
ticket_id: 2517f1ef-f9c4-4ba1-bb73-85504d211c1e
updated: 2026-11-16
status: inbox
sources:
  - ticket:2517f1ef-f9c4-4ba1-bb73-85504d211c1e
  - ticket:f410098b-6bd6-491f-9fb2-a9ede2f4d77d
  - https://github.com/yoosungung/scanbooks/pull/4
---

# scanbooks M1 파리티 픽스처 intent: pass

- Goal: `engine/tests/fixtures/` preprocess + `raw_flow→warped` + `raw_mask→inpainted` 기준 출력
- Diff: `engine/tests/fixtures/parity/` + preprocess/geo_warp/finger_inpaint refs; 수치 허용오차(해시 금지)
- PR #4 MERGED `38dfe987`; IC pytest 23 passed; CI checks N/A
- Pitfall: milestone 코멘트의 `@IC` 표기가 false Active wake를 유발 — IC 멘션은 child에만
- Next: ONNX 양자화 후보 `0be42506-ebb3-4175-909c-3eb656a3307e`
