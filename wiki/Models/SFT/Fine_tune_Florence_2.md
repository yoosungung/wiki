---
title: "Fine_tune_Florence_2"
related_raw: ["[[wiki/Models/SFT/Fine_tune_Florence_2.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_models']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

---
**출처**: [원본 링크](https://huggingface.co/merve/smol-vision/blob/main/Fine_tune_Florence_2.ipynb)
---

# Florence-2 모델 DocVQA 데이터셋 미세 조정

이 Jupyter Notebook은 Microsoft의 Florence-2 비전-언어 모델을 DocVQA 데이터셋에 미세 조정하여 문서 질의응답 작업을 수행하는 방법을 보여줍니다. 이 노트북은 종속성 설치, Hugging Face에서 DocVQA 데이터셋 로드, 사전 훈련된 Florence-2 모델 및 프로세서 로드, 기준 성능 확인을 위한 초기 추론 수행, DocVQA를 위한 사용자 정의 데이터셋 클래스 구축, 데이터 로더 설정, 그리고 최종적으로 모델 훈련 과정을 다룹니다. 또한 리소스 사용량을 줄이기 위해 이미지 인코더를 고정하는 방법과 미세 조정된 모델을 Hugging Face Hub에 푸시하는 방법도 언급합니다.

**추출된 URL:**
*   `https://huggingface.co/merve/smol-vision/blob/main/Fine_tune_Florence_2.ipynb`
*   `https://huggingface.co/front/assets/huggingface_logo-noborder.sv`
*   `https://huggingface.co/microsoft/Florence-2-base-ft`
*   `https://huggingface.co/HuggingFaceM4/DocumentVQA`
*   `https://huggingface.co/HuggingFaceM4/Florence-2-FT-DocVQA`
