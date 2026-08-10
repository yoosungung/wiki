---
id: vscode-extension-pure-core-host-split
title: "VS Code 확장: vscode-free core + host 어댑터 분리"
status: canonical
owner: km
updated: "2026-08-10"
last_updated: "2026-08-10"
review_after: "2026-11-10"
sources:
  - https://doi.org/10.48550/arxiv.2602.20206
  - ticket:458
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



## Host Gate + Heuristic Mirror (개념)

| 구성 | 요지 |
| :--- | :--- |
| Host Gate | SCM/husky 대신 확장 커맨드(예: `*.triggerGate`)를 기본 훅으로 두고, 호스트 어댑터만 VS Code API에 묶는다 |
| MirrorAdapter | 런타임(Ollama/node-llama 등) 확정 전 **HeuristicMirrorAdapter**를 기본으로 두고 인터페이스만 고정 |
| 스모크 | `runGateSmoke`로 none/light/full(+ sessionLoad downshift)을 **Electron 없이** 검증 |

ChangeScore·friction tier는 [[wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md]].

## 🔗 관련 문서

- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
