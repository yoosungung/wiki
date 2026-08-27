---
title: "Cloudflare OS 오픈소스 AI 생산성 워크스페이스 및 보안 아키텍처"
related_raw: ["[[raw/Cloudflare Open-Sources AI Productivity Workspace Cloudflare OS | Sumanth P님이 토픽에 대해 올림.md]]"]
tags: ['#inbox', '#Cloudflare-OS', '#AI-Agent', '#Sandboxing', '#Zero-Trust']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# Cloudflare OS 오픈소스 AI 생산성 워크스페이스 및 보안 아키텍처

## 1. 개요
* **정의**: Cloudflare가 사내에서 엔지니어링, 영업 등 다방면의 부서 임직원들이 자율 에이전트와 협업하기 위해 자체적으로 구축·사용하던 AI 생산성 워크스페이스인 **Cloudflare OS**(v2 기반)를 오픈소스로 공개했습니다.
* **배경 아키텍처**: 기존의 공유 SaaS 방식에서 벗어나, 개별 사용자를 위해 격리된 앱 샌드박스를 동적으로 생성하고, 보안 제어와 비동기식 승인 모델을 시스템 하단에 내재화한 점이 특징입니다.

## 2. 핵심 아키텍처 개념 (Gadgets & Gatekeepers)
Cloudflare OS는 AI 에이전트가 안전하게 작동하도록 돕기 위해 운영체제(OS) 수준의 격리 개념을 구체화했습니다.

### ① 가젯 (Gadgets) - 프라이빗 샌드박스 앱
* 사용자가 앱(예: 슬라이드 제작 툴)을 띄우면, 클라우드 상의 공용 SaaS 서버가 아니라 오직 해당 사용자만을 위한 독립된 샌드박스 가젯 인스턴스가 실행됩니다.
* **보안 격리**: 한 앱의 보안 결함이 타 사용자의 데이터 유출로 번질 수 없습니다.
* **AI 수정 가능 (AI-modifiable)**: 격리된 개인 복사본이므로, 에이전트에게 필요한 새로운 기능을 즉흥적으로 개발해 추가해 달라고 안전하게 요청할 수 있습니다.
* **기술 스택**: Cloudflare Workers 기반으로 Durable Objects가 개별 워크스페이스를 관리하고, 가젯 자체는 Dynamic Worker Facet 위에서 구동됩니다. 클라이언트와 서버는 Cap'n Web RPC를 통해 iframe 장벽을 넘어 통신합니다.

### ② 게이트키퍼 (Gatekeepers) - 역량 기반 보안 및 비동기 인간 제어
* **기본 권한 0 (Capability-based Security)**: 에이전트는 기밀 시스템이나 인터넷 등에 기본적으로 접근할 수 없으며, 모든 리소스 바인딩은 명시적으로 승인받아야 합니다.
* **비동기 승인 모델 (Async Human-in-the-Loop)**: 에이전트가 액션을 수행할 때마다 실행을 중단하고 사용자의 확인을 대기하는 방식 대신, Gatekeeper가 액션을 로컬 가상 환경에서 시뮬레이션하여 에이전트의 작업 흐름을 끊지 않으면서(Non-blocking), 실제 수행할 액션은 대기열(Queue)에 적재하여 사용자가 나중에 일괄 승인(Bulk Approval)하거나 반려할 수 있도록 구현했습니다.

## 3. 핵심 기능 목록
* **Durable Objects**: 실시간 다중 사용자 협업 지원.
* **Blueprints**: 가젯의 원본 템플릿(설계도)을 공유하여 타 사용자가 즉시 자신만의 격리된 인스턴스를 복제할 수 있도록 지원.
* **Code Mode**: 에이전트가 스스로 코드를 작성하여 가젯을 생성, 빌드, 테스트 및 디버깅하는 기능.
