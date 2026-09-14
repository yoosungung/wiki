---
id: vscode-extension-pure-core-host-split
title: "VS Code 확장: vscode-free core + host 어댑터 분리"
status: canonical
owner: km
updated: "2026-09-14"
last_updated: "2026-09-14"
review_after: "2026-12-14"
sources:
  - https://doi.org/10.48550/arxiv.2602.20206
  - ticket:458
  - ticket:242
  - ticket:254
  - ticket:1983
  - https://www.npmjs.com/package/ts-morph
  - https://devblogs.microsoft.com/ise/testing-vscode-extensions-with-typescript/
  - https://www.richardkotze.com/coding/unit-test-mock-vs-code-extension-api-jest
  - inbox/codingland/2026-09-14-host-jest-vscode-virtual-mock.md
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
npm run compile   # core → host (fresh sync 후 dist/out wipe 대비)
npm run test:vscode  # Extension Host QA — compile core-first 필수
```

Host E2E 게이트·CDN fallback·xvfb는 [[wiki/Engineering/AI-Native-Engineering/VSCode-Extension-Host-QA-Gate.md]]. Cloud Mirror 옵트인·Sanitizer는 [[wiki/Engineering/AI-Native-Engineering/Extension-Sanitizer-Cloud-Mirror-OptIn.md]].

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

## Host Jest 단위 테스트 시 `vscode` 가상 모킹 (`{ virtual: true }`)

- **런타임 모듈 부재**: `@types/vscode`는 타입 정의 전용이며, Node.js 단위 테스트 환경에서는 실제 `vscode` 모듈을 resolve할 수 없다.
- **가상 모킹 패턴**: 무거운 Extension Host(`test:vscode`)를 띄우지 않고 호스트 어댑터/GateHost를 빠른 Jest(`npm test`)로 검증할 때, 테스트 파일 또는 `__mocks__/vscode`에서 `{ virtual: true }` 옵션으로 모킹한다:
  ```typescript
  // GateHost.test.ts
  jest.mock("vscode", () => ({
    workspace: {
      getConfiguration: jest.fn(() => ({
        get: jest.fn(),
      })),
    },
    window: {
      activeTextEditor: undefined,
    },
  }), { virtual: true });
  ```
- **의존성 격리**: 테스트 대상 코드가 실제 사용하는 최소한의 API만 모킹하고, 출력 패널(`getPanel().appendLine`) 등 UI 컴포넌트는 별도 모듈 stub으로 분리하여 의존성 오염을 차단한다.

## 🔗 관련 문서

- [[wiki/Agents/Coding-and-Engineering/000_Coding-and-Engineering-MOC.md]]
- [[wiki/Engineering/AI-Native-Engineering/Agentic-Software-Factory.md]]
