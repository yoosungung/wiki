---
id: vscode-extension-host-qa-gate
title: "VS Code Extension Host QA gate (`test:vscode`)"
status: canonical
owner: km
updated: "2026-09-07"
last_updated: "2026-09-07"
review_after: "2026-12-07"
sources:
  - ticket:556
  - ticket:1749
  - inbox/codingland/2026-09-07-1749-xvfb-soft-skip.md
  - https://code.visualstudio.com/api/working-with-extensions/testing-extension
  - https://code.visualstudio.com/api/working-with-extensions/continuous-integration
  - https://github.com/Microsoft/vscode-test-cli/
tags: ["Engineering", "AI-Native", "VSCode", "QA", "E2E"]
type: "wiki"
---

# VS Code Extension Host QA gate (`test:vscode`)

브라우저 `base_url` E2E가 아니라 **Extension Host** 스모크가 제품 게이트일 때, tenant `.factory/quality.yaml`의 `e2e.command`를 Host 하네스에 맞춘다.

## 스택

| 구성 | 요지 |
| :--- | :--- |
| CLI | `@vscode/test-cli` + `@vscode/test-electron` |
| 진입 | `extension/host/.vscode-test.mjs` — activate + 제품 gate 커맨드(예: `*.triggerGate`) |
| Linux CI/Pod | `DISPLAY` 없으면 `xvfb-run`; gtk/nss/gbm/asound 등 Electron deps |
| LaunchArgs | `--disable-gpu` / `--disable-gpu-sandbox` / `--no-sandbox` / `--disable-dev-shm-usage` — **테스트 하네스에만**, 제품 activation 경로에 넣지 않음 |

## xvfb soft-skip (PATH 부재)

Headless Linux에서 `DISPLAY`가 비고 `xvfb-run`이 PATH에 없으면, 래퍼가 `spawnSync('xvfb-run')` → **ENOENT로 전체 `ci`를 빨갛게** 만들 수 있다. 단위 테스트(`npm test`)는 항상 켜 두고, Host 스모크만:

1. PATH에 `xvfb-run` 존재 여부를 먼저 probe한다.
2. 없으면 stderr에 soft-skip 사유를 남기고 **exit 0** (다운로드/Electron spawn 전).
3. Host 커버리지가 필요한 러너는 xvfb 또는 실 DISPLAY를 공급한다 — soft-skip은 게이트 소음 완화이지 Host 면제 선언이 아니다.

`quality.yaml`/`DESIGN`에 soft-skip 계약을 한 줄 적어 두면 AA/QA가 “스킵 ≠ 실패”로 읽는다 — [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]].

## compile core-first

fresh tenant sync가 `core/dist`·`host/out`을 지우면, host만 `compile -w`하면 `Cannot find module '@…/core'`가 난다.

```bash
# 개념: workspace compile과 동일하게 core → host
npm run test:vscode   # → npm run compile && … (core then host)
```

## CDN / 실행 파일 핀

잠긴 runner에서 `update.code.visualstudio.com`이 막히면 다운로드 래퍼가 **GitHub VSCodium tarball**로 fallback하거나 `VSCODE_EXECUTABLE_PATH`를 존중한다. 공급망 잔여를 줄이려면 CI에서 핀 경로를 우선한다.

다운로드/실행은 `spawnSync`/`execFileSync` **고정 argv + `shell:false`**, HTTPS redirect cap.

## AA / quality.yaml

`security.command`가 없으면 mechanical skip + 스코프 수동 리뷰(auth/Host/secret/transport). Host QA 게이트 델타(하네스·quality pointer)를 Deploying Test/prod 표면과 혼동하지 않는다.

## 🔗 관련 문서

- [[wiki/Agents/Coding-and-Engineering/VSCode-Extension-Pure-Core-Host-Split.md]]
- [[wiki/Engineering/AI-Native-Engineering/Tenant-Quality-Yaml-Gate-Skip-Pattern.md]]
- [[wiki/Engineering/AI-Native-Engineering/Epistemic-Debt-ChangeScore-Friction-Gate.md]]
