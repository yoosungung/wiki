---
title: "온디바이스 AI 및 AI PC 기술 트렌드 (2026)"
tags: ["On-Device", "AI-PC", "NPU", "Lunar-Lake", "Strix-Point", "Copilot+", "Agentic-AI"]
type: "wiki"
status: "published"
last_updated: "2026-08-30"
updated: "2026-08-30"
related_raw: ["[[raw/2026-08-30-on-device-ai-pc-spark-gorgon-panther.md]]", "[[raw/2026-08-28-on-device-ai-trends-rtx-spark-strix-halo-panther-lake.md]]", "[[2026-08-27-on_device_ai_trends_2026_uma.md]]", "[[2026-08-23-panther-lake-npu5-realworld-llm-benchmarks.md]]", "[[2026-06-15-On-Device-AI-PC-Trends-Update.md]]", "[[2026-06-17-Research-Synthesis-Update.md]]", "[[2026-06-26-on_device_ai_pc_agentic_trends.md]]", "[[2026-06-28-on_device_ai_trends_and_agentic_ai_2026.md]]", "[[2026-06-30-on_device_ai_trends_intel_amd_nvidia.md]]", "[[2026-07-01-on-device-ai-pc-hardware-trends.md]]", "[[2026-07-07-on-device-ai-trends-2026-ryzen-ai-max-panther-lake-rtx-spark.md]]", "[[2026-07-11-on_device_ai_pc_trends_strix_halo_panther_lake_rtx_spark.md]]", "[[2026-07-12-on-device-ai-pc-ryzen-ai-halo-npu-reality.md]]", "[[2026-07-13-ryzen-ai-halo-developer-center-bkc.md]]", "[[2026-07-17-ryzen-ai-halo-phoronix-shipping.md]]"]
---

# 💻 온디바이스 AI 및 AI PC 기술 트렌드 (2026)

2026년 온디바이스 AI 시장은 단순한 가속기 탑재를 넘어, 사용자의 워크플로우를 스스로 수행하는 **'에이전틱 AI(Agentic AI)'** 환경으로 진화했습니다.

## 1. 하드웨어 플랫폼 (AI PC 3파전)

| 제조사 | 플랫폼 | 주요 사양 | 핵심 포지셔닝 |
| :--- | :--- | :--- | :--- |
| **Intel** | **Lunar Lake (Core Ultra 2) / Panther Lake (Core Ultra 3)** | Intel 18A 공정 / NPU 5 (~50 TOPS, FP8 native 지원) / Xe3-LPG (Battlemage) iGPU (~120 TOPS) / Up to 128GB RAM | 30~70B 파라미터 로컬 모델 구동 가능. Lunar Lake의 NPU 4(48 TOPS) 대비 Panther Lake NPU 5는 플랫폼 총 180 TOPS 처리 지원(CPU, GPU, NPU 분산) 및 높은 면적 효율성 확보. (2026-07-08 업데이트) Panther Lake는 NPU 5(50 TOPS)와 Xe3-LPG GPU(120 TOPS)를 조합하여 경량 상시 AI 연산과 집중형 생성 AI 워크로드를 하이브리드로 완벽 분산 처리합니다. |
| **AMD** | **Strix Halo / Gorgon Halo (Ryzen AI Max 300)** | 16 'Zen 5' CPU cores / Radeon 8060S (40 RDNA 3.5 CUs) / XDNA 2 NPU (50 TOPS) / Up to 128GB (Strix) → **192GB (Gorgon Halo, 2026 H2)** Unified LPDDR5X | **PS5 / RTX 4060급 GPU 성능** 통합. Strix Halo는 128GB unified memory로 70B~200B 모델 로컬 추론 지원. **Gorgon Halo**는 Computex 2026에서 RTX Spark 대응 SKU로 192GB 메모리 확장을 예고. (2026-07-11 PM 업데이트) |
| **NVIDIA** | **RTX Spark / RTX GPU** | **1 Petaflop (FP4)** / 20-core Arm CPU (MediaTek) + Blackwell RTX GPU / 70B transistors (TSMC 3nm) / 128GB Unified LPDDR5X | GTC Taipei/COMPUTEX 2026 공식 런칭. **120B 로컬 에이전트 + 1M 토큰 컨텍스트** 목표. Microsoft **OpenShell** + Windows 보안 프리미티브로 primary PC 에이전트 샌드박스. Adobe Photoshop/Premiere 네이티브 재설계. (2026-07-11 PM 업데이트) |
| **Qualcomm** | **Snapdragon X2** | NPU 80+ TOPS | Always-On 연결성 및 저전력 배터리 특화. |

## 2. Windows Copilot+ 생태계 변화 (2026.06)
Microsoft의 Copilot+ 업데이트는 AI 성능의 가시화와 범용성에 초점을 맞추고 있습니다.

- **Agentic OS (OpenShell)**: Microsoft와 NVIDIA의 협업으로 탄생한 **OpenShell** 런타임을 통해 로컬 에이전트가 안전하게 OS 기능을 수행합니다.
- **Windows Primitives (에이전트 인프라)**:
    - **MXC (Microsoft Execution Containers)**: 에이전트 샌드박스용 커널 레벨 컨테이너. 무단 시스템 접근 시 프로세스 강제 종료.
    - **Agent Identity (Entra)**: 에이전트별로 고유 ID를 부여하여 인적 자원처럼 권한을 통제.
    - **Aion 1.0 Plan**: Windows에 기본 탑재된 14B 파라미터 추론 모델로, 클라우드 연결 없이 로컬 도구 호출 및 오케스트레이션 수행.
- **NPU 가시성**: 작업 관리자에 NPU 전용 탭이 추가되어 앱별 연산 점유율 모니터링 가능.

## 3. 로컬 에이전트 및 하이브리드 서빙
- **온디바이스 기본값(Default On-Device)**: 2026년 소비자 가전 및 PC 생태계는 클라우드 의존에서 온디바이스 NPU 처리를 기본값으로 가집니다. 디바이스 내부에서 개인정보(사진, 건강, 메시지 등)를 직접 처리함으로써 저지연, 오프라인 동작, 극대화된 프라이버시 보호가 제공됩니다.
- **하이브리드 아키텍처**: 빅테크 3사(Google, Apple, Samsung) 등은 로컬 장치가 1차 코어 태스크를 처리하고 고난도 추론만 클라우드로 이관하는 지능형 분산 하이브리드 설계를 적극 활용합니다.
  - **Always-on 태스크 (NPU)**: 노이즈 캔슬링, 아이콘텍 정렬, 개인 비서 등.
  - **Burst/Complex 태스크 (iGPU/GPU/Cloud)**: 복잡한 이미지 생성 및 문서 종합 추론.
- **Local Agentic AI**: OpenClaw 등 MAS 프레임워크가 AI PC의 NPU를 직접 활용하여 이메일 관리, 코드 작성, 시스템 설정을 자율적으로 수행합니다.
- **통합 메모리(Unified Memory)의 중요성**: 2026년에는 NPU TOPS 수치보다 **대용량 통합 메모리(128GB~192GB)** 확보가 "Frontier" 급 모델을 로컬에서 구동하기 위한 핵심 지표로 부상했습니다. **Strix Halo**가 이 시장을 주도하고 있습니다.

## 4. Ryzen AI Halo 출하 및 NPU vs iGPU 현실 (2026-07-12 업데이트)

### AMD Ryzen AI Halo (Strix Halo Mini PC)
- **Ryzen AI Max+ 395** 기반 미니 PC 출하: 128GB LPDDR5x-8000 UMA, Radeon 8060S, ~**120W TDP**.
- 소프트웨어: Debian 계열 **AMD Ryzen AI Developer Platform**, Lemonade Server / LM Studio / 에이전틱 플레이북(n8n) 문서화.
- 포지셔닝: NVIDIA **DGX Spark / RTX Spark** 대응. 후속 **Gorgon Halo(Ryzen AI Max 400)** 는 최대 **192GB** UMA 예고.

### NPU TOPS ≠ LLM 속도
- Copilot+ **40+ TOPS** 는 Windows AI 기능 게이트이며, 대형 로컬 LLM 성능을 보장하지 않음.
- 주류 NPU 경로 천장: 약 **~4B** 파라미터, Phi Silica ~**20 tok/s**.
- Autoregressive decode는 **메모리 대역폭 바운드**. Ollama/llama.cpp/LM Studio는 기본으로 **iGPU/CPU** 경로를 사용(NPU는 ONNX+QNN/OpenVINO 옵트인).
- 예외: Max+ 395에서 양자화 **70B ~14 tok/s** — 작업은 **iGPU**(최대 ~96GB 할당)에서 수행되며 NPU가 아님.
- Windows AI Foundry는 NPU 전용에서 GPU/CPU 경로로 확장 중(Phi Silica on GPU experimental).

### Developer Center · BKC · Playbooks (2026-07-13 PM)
[LTT Labs (2026-07-06)](https://www.lttlabs.com/articles/2026/07/06/amd-ryzen-ai-halo) 기준, Halo의 차별점은 실리콘보다 **1st-party 소프트웨어 번들**이다.
- 부팅 시 **Ryzen AI Developer Center**가 드라이버·Lemonade/LM Studio·PyTorch/VS Code·Comfy 등 개발 스택을 유지보수.
- Windows / Debian계 **AMD Ryzen AI Developer Platform**용 큐레이션 **BKC** 제공(팩토리 이미지 간 자유 전환은 제한적).
- **Playbooks**: n8n 등 에이전틱 툴 설치, 네트워크 경유 메트릭·원격 VS Code/Jupyter/터미널.
- 타사 Strix Halo 미니 PC 대비 가치: 동일 Max+ 395라도 큐레이션 OS·지속 지원이 AI 개발 온보딩 비용을 낮춤.
- 클러스터: DGX Spark식 QSFP(ConnectX-7) 없음 → **10GbE** 기반 클러스터링으로 우회.

### Phoronix 출하 확인 · 폼팩터 (2026-07-17 업데이트)
[Phoronix](https://www.phoronix.com/review/amd-ryzen-ai-halo)가 독립 Linux 리뷰와 함께 **정식 출하 시작**을 확인했습니다.
- 섀시: **150×150×45 mm**, **<1.2 kg**, TDP **120 W**.
- I/O: USB-C×3(PD), **10 GbE**, Wi‑Fi 7, BT 5.4, HDMI **2.1b** 단일(전용 DP 없음, USB-C→DP 가능), **2TB** PCIe Gen5 NVMe.
- 소프트웨어: Debian계 **AMD Ryzen AI Developer Platform**이 단순 Ubuntu+ROCm 이미지 이상이라는 점을 재확인.
- 출하 SKU는 Max+ 395(Strix Halo); Gorgon Halo(Max 400)는 후속.

## 4.2 실리콘 3사의 에이전틱 지향점 (2026-08-27 업데이트)

- **이종 가속기 및 UMA 분산 아키텍처**: 
  - **AMD Ryzen AI Max 300 / Max PRO 400 (Strix Halo)**: 16 Zen 5 코어 및 40 RDNA 3.5 CU GPU, 50 TOPS XDNA 2 NPU를 탑재. 128GB LPDDR5X 통합 메모리(UMA) 환경에서 dGPU 없이 고성능 로컬 추론을 제공하며, 기업용 보안을 갖춘 Max PRO 400 군을 통해 엔터프라이즈 모바일 워크스테이션급 에이전틱 가속을 실현합니다.
  - **Intel Panther Lake (Core Ultra 3)**: 인텔 18A 공정, Cougar Cove(P-core) 및 Darkmont(E-core) 코어. Xe3-LPG Battlemage GPU(120 TOPS)와 NPU 5(50 TOPS)를 묶어 플랫폼 합산 최대 180 TOPS의 가속을 띱니다. 평시 백그라운드 상시 모니터링은 저전력 NPU로, 버스트 연산은 GPU로 오프로딩하는 전력-성능 밸런싱이 핵심입니다.
  - **NVIDIA RTX Spark**: 20코어 Grace CPU(Arm) + Blackwell RTX GPU 기반 "슈퍼칩" 플랫폼. 최대 128GB Unified LPDDR5X 메모리 지원, FP4 기준 1 Petaflop의 강력한 연산 성능으로 120B급 대형 로컬 LLM(100만 토큰 컨텍스트)을 로컬 구동합니다. Microsoft OpenShell을 통해 자율 에이전트의 로컬 실행을 보장합니다.
- **Unified Memory (UMA) 가치 격상 및 Local Agentic AI**: 
  - 에이전틱 워크로드의 상시 자율 구동과 멀티턴 대화 상태 유지를 위해, CPU/GPU/NPU가 메모리를 공유함으로써 복잡한 대형 멀티모달 모델 구동 시 데이터 전송 병목을 원천 해소하는 UMA가 필수 지표로 자리 잡았습니다.
  - 로컬 자율 에이전트의 신뢰성과 보안이 주요 아젠다로 부상하면서, 단순 툴 호출을 넘어 MCP(Model Context Protocol) 표준과 폐쇄형 평가(closed-loop eval) 거버넌스를 통해 로컬 상에서 예외 처리 및 가드레일을 통제하는 아키텍처가 확산되고 있습니다.

## 5. Panther Lake NPU 5 실측·경쟁 비교 (2026-08-23)

CES 2026 이후 독립 리뷰·실측이 공개되면서, **Core Ultra Series 3 (Panther Lake)** 의 AI 성능이 스펙 슬라이드를 넘어 일상 사용 가능 여부로 평가되기 시작했습니다.

| 지표 | Panther Lake (X9 388H) | 비교·맥락 |
| :--- | :--- | :--- |
| NPU | **NPU 5, 50 INT8 TOPS** | Copilot+ PC 인증(≥40 TOPS) 충족 |
| 플랫폼 합산 | 최대 **180 TOPS** | GPU INT2/INT4 기여 포함 — 지속 추론에는 NPU 지표가 더 현실적 |
| LLM (Llama 3.1 8B) | NPU **~20 tok/s**, GPU **~25 tok/s** | 사람 읽기 속도(4–5 tok/s) 대비 체감 가능 수준 |
| vs AMD XDNA2 | Intel 주장 **4.3×** LLM 추론 (vs Ryzen AI 9 HX 370) | HotHardware CES 2026 |
| Geekbench AI | **~55k–56k** | Snapdragon X2 Elite Extreme **~88,615** (NPU 80+ TOPS) — 경쟁 격차 존재 |

**SKU·I/O 주의**: 플래그십 X 시리즈는 **PCIe 12레인**(H 시리즈 20레인). dGPU·고속 NVMe 구성 시 SKU 선택이 성능 병목이 될 수 있다.

**함정**: 180 TOPS 헤드라인은 마케팅 합산치이며, 대형 로컬 LLM·장시간 에이전트 워크로드는 여전히 **iGPU/GPU·대용량 UMA** 경로가 주류다. NPU는 Windows AI 기능·소형 모델 상시 추론에 최적.

출처: [vibetric Panther Lake 리뷰](https://vibetric.com/intel-panther-lake-review-2026/) · [Intel Newsroom](https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a)

## 6. 향후 과제
- **RAM 증설의 압박**: 로컬 LLM 및 에이전트의 멀티태스킹을 위해 **32GB RAM**이 최소 사양으로 요구되고 있습니다.
- **통합 메모리 대역폭**: NPU 성능만큼이나 메모리 대역폭(LPDDR5x/LPDDR6) 확보가 온디바이스 성능의 척도가 되고 있습니다.
- **구매 매트릭스**: Copilot+ AI PC(배터리·Windows AI) vs 96GB+ UMA/dGPU 머신(30B+ 로컬 LLM)을 목적별로 분리.

---
**관련 문서**:
- [[wiki/Models/Optimization-and-Serving/스마트폰-환경의-LLM-서빙-기술-2026]]
- [[wiki/Models/Optimization-and-Serving/리벨리온-ATOM-Max-기반-EXAONE-4.5-최적화-가이드]]
