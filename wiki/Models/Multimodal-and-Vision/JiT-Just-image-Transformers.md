---
title: "JiT-Just-image-Transformers"
related_raw: ["[[wiki/Models/Multimodal-and-Vision/JiT-Just-image-Transformers.md]]"]
tags: ['wiki', 'ai_core', 'llm_concepts', 'llm_architecture_and_technical']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

# JiT (Just image Transformers)

MIT의 새로운 논문 "Back to Basics: Let Denoising Generative Models Denoise"가 기존 확산(diffusion) 모델의 패러다임을 근본적으로 뒤흔들고 있습니다. 이 논문은 수년간 확산 모델이 "노이즈를 예측하는 것"을 생성의 핵심으로 여겨왔지만, 이는 잘못된 전제이며 모델이 "깨끗한 이미지를 직접 예측(x-pred)"해야 한다고 주장합니다.

이러한 변화는 모델에 안정성을 부여하고, 고해상도에서도 붕괴하지 않으며, Vision Transformer만으로도 고품질 이미지를 생성할 수 있게 합니다. MIT는 이 접근 방식을 "JiT (Just image Transformers)"라고 명명했습니다.

논문은 기존 확산 모델이 "데이터 매니폴드" 밖의 노이즈를 예측하도록 지시받았기 때문에 고차원에서 불안정하고 붕괴하는 근본적인 원인이 있었다고 비판합니다. 스파이럴 실험을 통해 노이즈 기반 예측이 고차원에서 형태를 붕괴시키는 반면, x-pred는 안정적으로 구조를 유지함을 보여줍니다.

JiT 모델은 VAE, 잠재 토크나이저, 지각 손실, 사전 학습 없이도 극도로 단순하게 설계되었음에도 불구하고 256, 512, 1024 해상도까지 자연스럽게 확장되며 붕괴하지 않습니다. MIT는 "노이즈 예측을 멈추면 스케일링이 사소해진다"고 강조합니다.

또한, 임베딩 병목 실험을 통해 임베딩 차원을 줄일수록 오히려 이미지 품질이 개선되는 현상을 발견했습니다. 이는 좁은 병목이 모델을 매니폴드 근처로 강제 정렬시켜 off-manifold 노이즈 표현을 억제하기 때문입니다.

결론적으로, 기존 확산 모델의 복잡한 기법들은 "노이즈 예측이라는 잘못된 목표를 보완하기 위한 임시방편"이었으며, MIT는 "이미지는 매니폴드 위에 있으니 이미지를 직접 예측하라"고 선언합니다. 이는 생성 모델의 문제 정의 자체를 다시 쓰는 혁신이며, 미래 생성형 AI가 훨씬 단순하고 안정적이며 확장성 있는 새로운 패러다임로 이동할 것임을 시사합니다. 우리는 지금 확산 이후의 시대, JiT 시대의 개막을 목격하고 있을지도 모릅니다.

[출처](https://www.linkedin.com/posts/suk-hyun-kim-31ba9b369_ai-suaqtztfmqvz-diffusion-activity-7397761042635968513-Pbni?utm_source=share&utm_medium=member_ios&rcm=ACoAADm5eyABU_duDuXv1f9N-6JhXB_iNO6faes)
