---
title: "Hugging Face 로컬 음성 에이전트(VAD-STT-LLM-TTS) 파이프라인 아키텍처"
related_raw: ["[[raw/Build Local Voice Agent with HuggingFace and OpenAI | AI Engineering님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#Voice-Agent', '#HuggingFace', '#OpenAI-Realtime', '#On-Device-AI']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Hugging Face 로컬 음성 에이전트(VAD-STT-LLM-TTS) 파이프라인 아키텍처

## 1. 개요
* **정의**: Hugging Face에서 로컬 LLM 및 오픈소스 오디오 모델들을 조합하여 전체 음성 에이전트 루프(VAD $\rightarrow$ STT $\rightarrow$ LLM $\rightarrow$ TTS)를 구동할 수 있는 통합 파이썬 패키지를 공개했습니다.
* **프로토콜 호환**: OpenAI Realtime API 규격과 호환되는 WebSocket API를 노출하여 기존 클라이언트 코드의 수정을 최소화합니다.
* **실제 적용**: Reachy Mini 로봇 수천 대의 상용 음성 백엔드로 채택되어 검증되었습니다.

## 2. 모듈별 스펙 및 대체 컴포넌트 (Modular Architecture)
모든 컴포넌트가 플러그인 형태로 분리되어 자유롭게 교환할 수 있습니다:
1. **음성 활동 감지 (VAD - Voice Activity Detection)**:
   - 기본 탑재: **Silero VAD v5** (발화 시작 및 대화 턴 넘김 감지).
2. **음성 인식 (STT - Speech-to-Text)**:
   - 기본 탑재: **Parakeet TDT** (유럽 25개 언어 기본 지원).
   - 대체 가능: Whisper, Faster Whisper, Paraformer 등.
3. **추론 엔진 (LLM)**:
   - OpenAI 호환 API 규격을 갖춘 모든 로컬/클라우드 엔드포인트 연동 가능.
   - 예: 로컬 `llama.cpp` 또는 vLLM 서버, 클라우드 OpenRouter 등.
4. **음성 합성 (TTS - Text-to-Speech)**:
   - 기본 탑재: **Qwen3-TTS** (로컬 고품질 음성 출력).
   - 대체 가능: Kokoro, ChatTTS, Pocket TTS, MMS TTS 등.

## 3. 기능 및 실행 모드
* **4가지 런타임 인터페이스**:
  - 실시간 WebSocket 서버
  - 로컬 오디오 입출력 인터페이스
  - 로우(Raw) WebSocket 연결
  - TCP 소켓 방식
* **다국어 자동 감지**: 대화 턴 사이에 언어가 변경되어도 자동으로 언어를 판별 및 처리합니다.
* **배포 최적화**: GPU 가속 인프라 배포를 돕기 위한 Docker 환경을 지원합니다.
