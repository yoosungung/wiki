---
id: inbox-codingland-host-jest-vscode-virtual-mock
agent: codingland
ticket_id: 1983
updated: 2026-09-14
status: inbox
sources:
  - ticket:1983
  - https://devblogs.microsoft.com/ise/testing-vscode-extensions-with-typescript/
  - https://www.richardkotze.com/coding/unit-test-mock-vs-code-extension-api-jest
---

# Host Jest: mock `vscode` with `{ virtual: true }`

- `@types/vscode` is types-only; Node cannot resolve the `vscode` module in host unit tests.
- Prefer `jest.mock("vscode", factory, { virtual: true })` in the test file (or `__mocks__/vscode` + `moduleNameMapper`) so GateHost/panel adapters can run under `jest` without Extension Host.
- Mock only APIs touched (`workspace.getConfiguration`, `window.activeTextEditor`); stub `./panel` `getPanel().appendLine` separately.
