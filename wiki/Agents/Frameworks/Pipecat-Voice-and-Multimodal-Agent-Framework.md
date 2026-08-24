---
title: "Pipecat: 실시간 음성 및 멀티모달 대화형 에이전트 프레임워크"
related_raw: ['[[2026-08-24-pipecat-multimodal-voice-agent-framework.md]]']
tags: ['Pipecat', 'Voice-Agents', 'Multimodal-AI']
type: "wiki"
status: "published"
last_updated: "2026-08-24"
updated: "2026-08-24"
---

# 🎙️ Pipecat: 실시간 음성 및 멀티모달 대화형 에이전트 프레임워크

실시간 오디오/비디오 스트리밍 대화형 멀티모달 에이전트를 자율적으로 제어하기 위한 오픈소스 파이썬 프레임워크입니다.

## 1. 주요 기능 레이어
- **다중 서비스 오케스트레이션**: 다양한 LLM, ASR(음성 인식), TTS(음성 합성), VLM(비전 모델)을 파이프라인으로 연결.
- **전송 계층(Transport) 최적화**: WebRTC, Daily, WebSocket 등 저지연 미디어 전송 인프라 통합.
- **대화 제어 버스**: 다자간 대화, 에이전트 간 업무 인계(Handoff) 및 shared bus 기반의 오케스트레이션 구조를 로컬 및 분산 네트워크 상에서 구현 가능.

---
**관련 문서**:
- [[wiki/Agents/Frameworks/AgentENV-High-Performance-RL-Sandbox.md]]
