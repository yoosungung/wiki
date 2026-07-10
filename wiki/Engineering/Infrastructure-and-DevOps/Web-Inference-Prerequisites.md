---
title: "브라우저 기반 AI 추론을 위한 기술적 전제 조건 (Web Inference Prerequisites)"
status: "published"
category: "Engineering"
subcategory: "Infrastructure-and-DevOps"
tags: [Security, Cross-Origin-Isolation, COOP, COEP, WebNN]
last_updated: "2026-05-13"
related_raw: [
  "[[raw/2026-05-12-making-your-website-cross-origin-isolated.md]]",
  "[[raw/2026-05-12-cross-origin-embedder-policy-coep-header.md]]",
  "[[raw/2026-03-27-Web-Neural-Network-API.md]]"
]
---

# 브라우저 기반 AI 추론을 위한 기술적 전제 조건

고성능 브라우저 기반 AI 추론(예: LLM 실행)을 구현하기 위해서는 단순한 라이브러리 도입 외에 브라우저 보안 환경 및 전용 API에 대한 이해와 설정이 필수적입니다.

## 1. 교차 출처 격리 (Cross-Origin Isolation)

`SharedArrayBuffer`와 같은 강력한 기능을 사용하여 멀티 스레딩 및 메모리 공유를 최적화하려면 웹사이트가 "교차 출처 격리" 상태여야 합니다. 이는 Spectre와 같은 사이드 채널 공격을 방지하기 위한 브라우저의 보안 요구 사항입니다.

### 필수 HTTP 헤더 설정
메인 문서 응답 시 다음 헤더를 포함해야 합니다:
- **COOP (Cross-Origin-Opener-Policy)**: `same-origin`
- **COEP (Cross-Origin-Embedder-Policy)**: `require-corp` 또는 `credentialless`

### 격리 상태 확인
JavaScript에서 `self.crossOriginIsolated` 값이 `true`인지 확인하여 격리 성공 여부를 판단할 수 있습니다.

## 2. SharedArrayBuffer 및 고정밀 타이머
교차 출처 격리가 활성화되면 다음 기능을 사용할 수 있습니다:
- **SharedArrayBuffer**: 웹 워커(Web Worker) 간에 메모리를 공유하여 대규모 텐서 데이터를 복사 없이 전달.
- **고정밀 타이머**: `performance.now()`의 해상도가 높아져 성능 프로파일링 및 최적화가 용이해짐.

## 3. Web Neural Network (WebNN) API
WebNN은 운영체제 및 하드웨어 플랫폼(NPU, GPU, CPU 가속기)의 머신러닝 성능을 직접 활용하기 위한 저수준 W3C 표준 API입니다.

- **목적**: 하드웨어 플랫폼에 구속되지 않는 추론 가속 레이어 제공.
- **이점**: WebGPU보다 더 머신러닝에 특화된 추론 프리미티브 제공, 데이터 프라이버시 강화.
- **보안**: 모든 입력 데이터(이미지, 오디오 등)를 브라우저 샌드박스 내에서 처리하여 외부 유출 차단.

## 관련 문서
- [[wiki/Models/Optimization-and-Serving/Browser-AI-Inference-MOC.md|Browser AI Inference MOC]]
- [[wiki/Models/Optimization-and-Serving/WebGPU-Acceleration.md|WebGPU 가속]]
