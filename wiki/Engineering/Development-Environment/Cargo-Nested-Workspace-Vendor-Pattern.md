---
id: cargo-nested-workspace-vendor-pattern
title: "Rust Cargo 중첩 워크스페이스(Nested Workspace) 벤더링 및 어댑터 패턴"
status: canonical
owner: km
updated: "2026-11-09"
last_updated: "2026-11-09"
sources:
  - inbox/rhwp_batch/2026-11-09-rhwp-upstream-v0.9.0-vendor-nest.md
  - inbox/rhwp_batch/2026-11-09-rhwp-upstream-v0.9.0-vendor-fonts.md
  - inbox/rhwp_batch/2026-11-09-rhwp-upstream-v0.9.0-tag-release.md
  - inbox/pm/2026-11-09-intent-pass-rhwp-v090-pr6.md
  - ticket:0f34dece-193b-4a93-bca5-6c8d408fb620
  - https://github.com/edwardkim/rhwp/releases/tag/v0.9.0
  - https://github.com/yoosungung/rhwp_batch/pull/6
  - inbox/rhwp_batch/2026-11-03-rhwp-upstream-v0.8.7-nest.md
  - ticket:2802d700-87fe-4f67-81b9-877a44fdbe08
  - https://github.com/edwardkim/rhwp/releases/tag/v0.8.7
tags: ["Engineering", "DevEnv", "Rust", "Cargo", "Vendoring", "Workspace"]
type: "wiki"
---

# Rust Cargo 중첩 워크스페이스(Nested Workspace) 벤더링 및 어댑터 패턴

## 1. 개요 및 문제 정의
Rust의 Cargo는 기본적으로 **워크스페이스 내부에 또 다른 `[workspace]`를 중첩(Nested Workspace)하는 것을 허용하지 않는다**. 업스트림 오픈소스 크레이트(예: `edwardkim/rhwp` v0.8.7+)가 단일 크레이트에서 루트 `[workspace]`와 하위 경로 의존성(`crates/*`)을 가지는 멀티 크레이트 워크스페이스 구조로 전환될 경우, 이를 상위 워크스페이스(예: `rhwp_batch`) 하위 서브디렉터리로 벤더링(Vendoring)하면 Cargo 매니페스트 파싱 충돌이 발생한다.

이 문서는 업스트림 Rust 소스 코드(`.rs`)를 직접 패치하지 않고 **매니페스트 어댑터(Nest Adapter)**만으로 중첩 워크스페이스를 깔끔하게 벤더링하는 표준 절차를 정의한다.

---

## 2. 핵심 설계 및 벤더링 절차

### 2.1 벤더링 복사 세트(Vendor Copy Set) 확장
업스트림이 단일 크레이트에서 멀티 크레이트 워크스페이스로 변경된 경우, 기존 `src/`, `Cargo.toml`, `examples/`, `saved/` 외에 다음 요소들을 반드시 벤더링 복사 세트에 포함해야 한다.
- `crates/*`: 업스트림 루트 크레이트가 `path = "crates/..."`로 참조하는 내부 하위 크레이트(예: `crates/rhwp-contracts`, `crates/rhwp-ooxml-chart`, `crates/rhwp-password-crypto`).
- `build.rs`: 컴파일 타임 코드 생성 또는 바인딩 스크립트.

### 2.2 매니페스트 중첩 어댑터 (Nest Adapter)
업스트림 `.rs` 비즈니스 로직은 수정하지 않고(Zero `.rs` Patch), 두 `Cargo.toml`의 워크스페이스 선언부만 조정한다.

1. **벤더링된 하위 `Cargo.toml`에서 `[workspace]` 섹션 제거**:
   - 벤더링된 디렉터리(예: `rhwp/Cargo.toml`)에 선언된 중첩 `[workspace]` 테이블을 스트립(strip)하여 일반 패키지 매니페스트로 전환한다.
   - 내부 `[dependencies]`의 상대 경로(`path = "crates/..."`)는 그대로 유지한다.
2. **상위 루트 `Cargo.toml`의 `members`에 하위 크레이트 편입**:
   - 상위 워크스페이스 루트 `Cargo.toml`의 `[workspace].members` 배열에 벤더링된 루트 크레이트와 하위 크레이트 글로브(`rhwp/crates/*`)를 함께 등록한다.

```toml
# 상위 루트 Cargo.toml 예시
[workspace]
resolver = "2"
members = [
    "rhwp-batch",
    "rhwp",
    "rhwp/crates/*",
]
```

---

## 3. 운영 함정 및 검증 가드레일

### 3.1 Gitignore된 테스트 픽스처(Fixtures) 동기화
- 벤더링된 크레이트나 배치 러너의 통합 테스트(`cargo test -p rhwp-batch`)가 저장소에서 `.gitignore` 처리된 샘플 파일(예: `rhwp-batch/samples/from_rhwp/*`, `rhwp/samples/basic/english.hwp`)을 참조하는 경우, CI나 새 체크아웃 환경에서 파일 누락으로 테스트가 실패한다.
- **해결**: 업스트림 릴리스 타르볼/태그의 `samples/` 디렉터리로부터 테스트 픽스처를 먼저 복사·배치한 뒤 `cargo test`를 실행한다.

### 3.2 만료된 `GH_TOKEN` 환경변수 우회 (Keyring Fallback)
- 셸 환경에 주입된 `GH_TOKEN`이 만료(401 Bad credentials)된 상태면 공개 리포지토리(`edwardkim/rhwp`)의 릴리스 태그 조회조차 실패한다.
- **해결**: `env -u GH_TOKEN gh release view v0.8.7 --repo edwardkim/rhwp`와 같이 환경변수를 언셋(`-u`)하여 OS 키링(Keyring) 인증 또는 공개 API 경로로 폴백한다.

---


## 4. v0.9.0 확장: `vendor/*` · fonts · workspace flatten

edwardkim/rhwp **v0.9.0**부터 default feature가 path vendor(`vendor/rhwp-pdf-import-backend`, `rhwp-zune-jpeg`, `rhwp-jpeg-encoder`, `svg2pdf`, hayro/qcms/codec 등)를 당긴다. 0.8.7 nest 어댑터(루트 `[workspace]` strip + `rhwp/crates/*` members)만으로는 부족하다.

### 4.1 Vendor copy-set

| 경로 | 이유 |
| :--- | :--- |
| `rhwp/vendor/` | path-dep 크레이트 본체 |
| `assets/fonts/*`, `assets/font-rules/*` | `include_bytes!`/`include_str!` — promo `chrome`/`edge` 없어도 **필수** |
| `src/`, `crates/`, `saved/`, `samples/` | 기존 세트 |
| `tools/` (~580MB) | `rhwp-batch` 미사용 — omit 가능 (0.8.7도 미포함) |

전체 upstream tarball은 multi-GB이므로 sparse clone/checkout(`src`,`crates`,`saved`,`samples`,`vendor`,`assets`)이 실용적이다.

### 4.2 Workspace inheritance flatten

`vendor/svg2pdf` 등은 `[workspace.package]`/`[workspace.dependencies]` inheritance(`{ workspace = true }`)를 쓴다. 루트 `[workspace]` strip만 하면 outer `rhwp_batch`에서 multiple-root / missing `workspace.package` 파싱 오류가 난다. **값을 패키지 매니페스트에 인라인 flatten**해야 한다.

### 4.3 Intent·Release 운영

- Intent: lean nest PR(fonts/font-rules only, 예: #6)을 fat vendor(#5 chrome/edge)보다 우선. Repo CI는 tag-only `release.yml` — PR checks 부재; 게이트는 `cargo test -p rhwp-batch`.
- Merge 후 annotated tag `v0.9.0`(force/retag 금지) → Release. macOS runner 라벨은 [[wiki/Engineering/AI-Native-Engineering/GHA-macOS-14-Runner-Retirement-Hotfix.md]].


## 🔗 관련 문서
- [[wiki/Engineering/Development-Environment/000_Development-Environment-MOC.md]]
- [[wiki/Engineering/AI-Native-Engineering/Factory-Schedule-Ops-Skips.md]]
- [[wiki/Engineering/AI-Native-Engineering/GHA-macOS-14-Runner-Retirement-Hotfix.md]]
- [[wiki/Engineering/AI-Native-Engineering/Wiki-Synthesis-Policy.md]]
