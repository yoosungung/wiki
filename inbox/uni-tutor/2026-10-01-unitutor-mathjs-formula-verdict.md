---
id: inbox-uni-tutor-mathjs-formula-verdict
agent: uni-tutor
ticket_id: a8ed07b1-dc58-4ca1-9582-381d0d9ae59f
updated: 2026-10-01
status: inbox
sources:
  - ticket:a8ed07b1-dc58-4ca1-9582-381d0d9ae59f
  - https://mathjs.org/docs/expressions/parsing.html
---

# UniTutor formulaVerdict — Math.js (not Pyodide)

- T3-02 수식 판정은 **Math.js** 채택. Pyodide는 초기 WASM·로드 비용으로 제외 (`frontend/DESIGN.md`).
- `checkFormula(learner, expected)` → `correct`|`incorrect`. 자유변수는 샘플 포인트 평가로 동치 판정 (`(x+1)^2` ≡ `x^2+2x+1`).
- `applyFormulaVerdict`가 `formulaVerdict`를 먼저 싣고 유도 질문만 교체. incorrect여도 정답/풀이 필드를 `TutorTurn`에 넣지 않음 (ARCHITECTURE §1).
