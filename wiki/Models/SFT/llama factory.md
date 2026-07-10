---
title: "llama factory"
related_raw: ["[[wiki/Models/SFT/llama factory.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_tools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

1. 설치
```
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git
pip install --no-deps xformers
pip install .[bitsandbytes]
```