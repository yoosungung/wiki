# 🌐 크로스 플랫폼 브라우저 환경의 LLM 서빙 기술 및 아키텍처 분석

## 1. 연구 목적 및 개요
브라우저 기반의 AI 추론은 클라우드 의존성을 낮추고 개인정보를 보호하며 인프라 비용을 절감하는 차세대 패러다임이다. 본 연구는 WebGPU 및 WebAssembly(WASM)를 활용하여 Windows, macOS, Android, iOS 등 다양한 플랫폼에서 LLM을 효율적으로 서빙하는 기술적 토대와 최적화 전략을 분석한다.

## 2. 핵심 기술 스택
- **WebAssembly (WASM) 3.0**: 오케스트레이션 및 CPU 연산 담당.
    - **Memory64**: 4GB 메모리 제한 극복 (최대 16GB 지원).
    - **SIMD / Relaxed SIMD**: 행렬 연산 가속.
- **WebGPU**: 하드웨어 가속(GPU) 담당.
    - WGSL을 통해 D3D12, Metal, Vulkan 등 네이티브 API 추상화.
    - 통합 메모리 아키텍처(Apple M-series)에서 네이티브 대비 80% 성능 구현.
- **WebNN**: NPU 직접 활용을 위한 미래 표준 API.

## 3. 주요 프레임워크 비교
| 항목 | WebLLM | Transformers.js |
| :--- | :--- | :--- |
| **백엔드** | WebGPU (TVM 최적화) | WebGPU, WASM (ONNX Runtime) |
| **특징** | PagedAttention, OpenAI 스타일 API | 허깅페이스 생태계, 멀티모달 지원 |
| **최적화** | MLC-LLM 기반 커널 최적화 | 다양한 양자화(q4, q8, fp16) 지원 |

## 4. 플랫폼별 특이사항
- **Desktop (Win/Mac)**: WebGPU 성숙도가 높으며, 특히 Mac M-series에서 높은 성능 보존율을 보임.
- **Android**: 하드웨어 파편화로 인해 WASM Fallback 전략 필수.
- **iOS**: 엄격한 WebKit 메모리 관리로 인해 1B~3B 수준의 SLM 또는 극단적 양자화 요구.

## 5. 한국어 모델 서빙 전략
- **추천 모델**: Yanolja EEVE 2.8B (높음), Solar Pro 2 (보통), HyperClova X (보통), Kanana Nano (매우 높음).
- **최적화**: 한국어 토크나이저 효율성이 높은 모델 선택 (Bytes-per-token 최적화).

## 6. 보안 및 프라이버시
- **Cross-Origin Isolation**: SharedArrayBuffer 활성화를 위한 COOP/COEP 헤더 설정 필수.
- **Privacy-by-default**: 로컬 추론을 통한 데이터 주권 확보.

## 7. 향후 로드맵 (2026+)
- WebNN 기반 NPU 가속기 활용 확대.
- 브라우저 내장 AI (Gemini Nano 등) API와의 통합 연구.

---
*참조 보고서: 크로스 플랫폼 브라우저 환경에서의 대규모 언어 모델 서빙 기술 및 아키텍처 분석 보고서 (2026)*
