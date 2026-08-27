---
title: "LLaMA Factory Fine Tuning"
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_tools']
type: "wiki"
status: "published"
---

# LLaMA Factory Fine-Tuning

LLaMA-Factory를 설치하고 환경을 구성하기 위한 명령어 안내입니다.

## 설치 방법

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps xformers
pip install .[bitsandbytes]
```
