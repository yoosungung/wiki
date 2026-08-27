---
title: "Kyutai Pocket TTS: CPU 기반 고속 로컬 TTS 엔진"
related_raw: ["[[raw/CPU-based text-to-speech for local AI agents | AI Engineering님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#TTS', '#Kyutai', '#On-Device-AI', '#CPU-Serving']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Kyutai Pocket TTS: CPU 기반 고속 로컬 TTS 엔진

## 1. 개요
* **정의**: Kyutai에서 개발한 **Pocket TTS**는 별도의 GPU 서버나 클라우드 API 호출 없이 오직 CPU만을 활용하여 엣지 디바이스나 로컬 개발 환경에서 빠르게 구동되는 100M(1억) 파라미터 규모의 고속 가량 음성 합성(TTS) 모델입니다.
* **장점**: AI 에이전트 파이프라인 구축 시 고비용 GPU 리소스 요건을 피하고 프라이버시가 보장되는 온디바이스 음성 피드백 루프를 실현할 수 있습니다.

## 2. 주요 성능 및 기술 사양
* **속도 및 리소스**: 2개의 CPU 코어만 사용하여 실시간 대비 6배 빠른($6\times$ real-time speed) 음성 합성을 처리합니다.
* **첫 청크 지연 시간(Latency)**: 첫 오디오 청크를 반환하기까지 약 200ms가 소요됩니다.
* **음성 복제 (Voice Cloning)**: 임의의 짧은 단일 WAV 파일 입력만으로도 해당 발화자의 목소리를 복제하여 음성을 생성해 낼 수 있습니다.
* **스트리밍 지원**: 합성이 완전히 끝나지 않더라도 실시간 오디오 스트리밍 출력을 지원합니다.
* **다국어 처리**: 영어, 프랑스어, 독일어, 포르투갈어, 이탈리아어, 스페인어 등 다국어 번역 발화를 지원합니다.

## 3. 개발 연동성
* **OpenAI 호환 API**: `pocket-tts serve` 명령어를 사용하여 실행하면 OpenAI 오디오 API 규격을 제공하는 로컬 HTTP 웹 서버로 동작하므로, 기존 애플리케이션의 Drop-in 대체가 쉽습니다.
* **텍스트 길이 무제한**: 긴 텍스트 입력 시 인위적인 텍스트 청킹(Chunking) 없이 한 번에 긴 처리가 가능합니다.
* **브라우저 구동**: 커뮤니티 구현체를 통해 WebAssembly(Wasm) 기반으로 웹 브라우저 로컬 샌드박스에서 직접 구동할 수 있습니다.
