---
id: vscode-extension-pure-core-host-split
title: "VS Code 확장: vscode-free core + host 어댑터 분리"
status: canonical
owner: km
updated: "2026-08-06"
last_updated: "2026-08-06"
review_after: "2026-11-06"
sources:
  - ticket:242
  - ticket:254
  - https://www.npmjs.com/package/ts-morph
tags: ["Agents", "Coding", "VSCode", "Extension", "AST", "ts-morph"]
type: "wiki"
---

# VS Code 확장: vscode-free core + host 어댑터 분리

Foam 스타일: **`extension/core`는 vscode-free**(Jest만), **`extension/host`는 VS Code 어댑터**. 도메인 그래프·프로토콜은 core에서 단위 테스트하고, Sidebar/Custom Editor/OutputChannel은 host stub.

## M0 골격(개념)

| 층 | 책임 |
| :--- | :--- |
| core | GraphDelta apply, AST fingerprint stub, 프로토콜 envelope parse |
| host | WebviewView, Custom Editor canvas, Time Bar/Hot Reboot placeholder, `revealBeside` |

```bash
# extension/ 기준
npm test          # core ~초 단위
npm run compile
```

## TS/JS AST 추출

- in-process **ts-morph**로 `extracted` call/contains 엣지(tree-sitter는 다언어 단계로 연기).
- Debt meter는 **extracted** 노드만 집계(`confidence` 기본 extracted).
- Semantic Zoom 시 landmark `anchor` 좌표 유지(Mental-Map Preserving).

## 🔗 관련 문서

- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
