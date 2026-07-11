---
title: "RunPod"
related_raw: ["[[wiki/Models/SFT/RunPod.md]]"]
tags: ['wiki', 'ai_core', 'fine-tuning_&_reasoning_models', 'fine-tuning_tools']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query": "mutation { podResume( input: { podId: \"inzk6tzuz833h5\", gpuCount: 1 } ) { id desiredStatus imageName env machineId machine { podHostId } } }"}'

curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query": "mutation { podStop(input: {podId: \"riixlu8oclhp\"}) { id desiredStatus } }"}'

curl --request POST \
  --header 'content-type: application/json' \
  --url 'https://api.runpod.io/graphql?api_key=${YOUR_API_KEY}' \
  --data '{"query":"mutation terminatePod($input: PodTerminateInput!) { podTerminate(input: $input) }"}'