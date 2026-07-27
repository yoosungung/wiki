---
title: 개발자용 상시 무료 클라우드 인프라 자원 정리 (free-for-dev)
last_updated: "2026-07-27"
updated: "2026-07-27"
related_raw: ["[[2026-07-27-free_infrastructure_services_for_developers.md]]"]
tags: [Infrastructure, DevOps, Free-Tier, Cloud-Compute]
---

# 개발자용 상시 무료 클라우드 인프라 자원 정리 (free-for-dev)

이 문서는 개발자가 사이드 프로젝트, 프로토타입 배포 및 에이전트 구동 서버를 돈을 쓰지 않고 영구적 혹은 장기적으로 구축할 수 있도록 지원하는 핵심 무료 티어(Free Tier) 인프라 서비스를 정리합니다.

## 1. Cloudflare 생태계 (가장 추천하는 인프라)

서버리스 및 프론트엔드/백엔드 스토리지를 완벽히 무료로 구축하는 최상의 생태계입니다.
- **Cloudflare Workers**: 하루 100,000회 무료 호출이 가능한 서버리스 V8 런타임 함수.
- **Cloudflare Pages**: 무제한 정적 웹사이트 배포 및 무제한 대역폭 호스팅.
- **R2 Storage**: egress(아웃바운드) 비용이 완전히 면제되는 10GB 오브젝트 스토리지.
- **D1 Database**: Cloudflare Workers 내에 이식해 활용할 수 있는 경량 SQL 데이터베이스.
- **Tunnel (로컬 노출)**: 로컬 호스트 포트를 별도 방화벽 설정 없이 외부 도메인 주소로 즉시 매핑시켜 노출해 주는 터널링 가상망 기능.

## 2. Oracle Cloud (OCI Always Free)

가장 풍부한 컴퓨팅 성능(VM)과 트래픽을 상시 무료로 보장합니다.
- **AMD VM**: 1/8 OCPU 및 1GB RAM을 갖춘 AMD Micro 인스턴스 2대 상시 무료.
- **ARM Ampere A1 VM**: 최대 4개 OCPU 및 24GB RAM을 보유한 고성능 ARM 서버 제공. (서버 1대로 24GB 구동하거나 여러 서버로 쪼개어 운용 가능)
- **네트워크 트래픽**: 매달 아웃바운드 대역폭 **10TB**를 영구 무료 제공. (서이드 프로젝트에 차고 넘치는 대역폭)

## 3. Google Cloud Platform (GCP Always Free)

개발용 서버리스 파이프라인 및 소형 인스턴스 운영에 특화되어 있습니다.
- **Compute Engine**: 미국 리전(Oregon, Iowa, South Carolina) 내 e2-micro 인스턴스 1대 상시 무료.
- **Cloud Functions**: 월 200만 회 호출 무료.
- **BigQuery**: 월 1TB 쿼리 분석 및 10GB 스토리지 제공.
- **Cloud Run**: 월 200만 요청 무료.
- **Gemini API (Google AI Studio)**: 분당 15회, 일 1,500회 호출 무료. (에이전트 개발 기초 테스트용 최적)

## 4. Amazon Web Services (AWS Free Tier)

서버리스 중심의 검증용 아키텍처에 적합합니다.
- **AWS Lambda**: 월 100만 회 호출 무료.
- **DynamoDB**: 25GB 스토리지 및 월 2억 회 읽기/쓰기 용량 무료.
- **Amazon S3**: 5GB 스토리지 및 20,000회 읽기 요청 무료.
- **Amazon CloudFront**: 아웃바운드 트래픽 월 1TB 무료.

---
## 🔗 관련 문서 링크
- 로컬 벡터 DB RAG 연동: [[wiki/RAG/KnowNote-Local-First-RAG-NotebookLM.md]]
- 에이전트 자율 테스팅 및 CI 결합: [[wiki/Agents/Evaluations/DeepEval-Evaluation-Framework.md]]
