---
title: "text generation web-ui 실행"
related_raw: ["[[wiki/Engineering/Development-Environment/text generation web-ui 실행.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'dev_setup_guides']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

1. 설치
```
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install peft gradio
pip install -r requirements.txt
pip install numba datasets accelerate
pip install -U deepspeed
pip install -i https://pypi.org/simple/ bitsandbytes
```

2. 실행
```
python server.py --chat --share --listen
```

3. load model
- https://huggingface.co/ 모델 download
- MaziyarPanahi/WizardLM-2-7B-GGUF

4. 
 