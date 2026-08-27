---
title: "RunPod Cloud GPU Inference"
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_tools']
type: "wiki"
status: "published"
---

# RunPod Cloud GPU Inference

RunPod의 GraphQL API를 활용하여 클라우드 GPU 인스턴스(Pod)를 제어하는 CLI 명령어 모음입니다.

## 주요 API 명령어 (cURL)

**Pod 재개 (Resume)**
```bash
curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query": "mutation { podResume( input: { podId: \"inzk6tzuz833h5\", gpuCount: 1 } ) { id desiredStatus imageName env machineId machine { podHostId } } }"}'
```

**Pod 중지 (Stop)**
```bash
curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query": "mutation { podStop(input: {podId: \"riixlu8oclhp\"}) { id desiredStatus } }"}'
```

**Pod 종료 (Terminate)**
```bash
curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query":"mutation terminatePod($input: PodTerminateInput!) { podTerminate(input: $input) }"}'
```
