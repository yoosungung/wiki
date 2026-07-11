---
title: "DGX Spark"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/DGX Spark.md]]"]
tags: ['wiki', 'engineering_and_infra', 'ai_development', 'dgx']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

### ssh
```sh
alias dgx1="ssh didimai@211.218.150.245 -p 50024"
alias dgx2="ssh didimai@211.218.150.246 -p 50024"
# password : <YOUR_PASSWORD>
```

### SGLang launch
```sh
docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<YOUR_HF_TOKEN>" \
    --ipc=host \
    nvcr.io/nvidia/sglang:25.10-py3 \
    python3 -m sglang.launch_server \
    --model-path Qwen/Qwen3-0.6B \
    --host 0.0.0.0 --port 30000
```
### vLLM launch
```sh
docker run --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<YOUR_HF_TOKEN>" \
    --env TIKTOKEN_ENCODINGS_BASE=/root/.cache/huggingface/hub \
    -p 8000:8000 \
    --ipc=host \
    nvcr.io/nvidia/vllm:25.09-py3 \
    python -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 \
    --model openai/gpt-oss-20b
```


### test
```sh
sudo nano /etc/hosts
---
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1 localhost
255.255.255.255 broadcasthost
::1             localhost

## DGX
211.218.150.245 dgx1
211.218.150.246 dgx2
```

```sh
% curl http://dgx1:30000/v1/models
{"object":"list","data":[{"id":"Qwen/Qwen3-0.6B","object":"model","created":1762912482,"owned_by":"sglang","root":"Qwen/Qwen3-0.6B","max_model_len":40960}]}

% curl http://dgx2:30000/v1/models
{"object":"list","data":[{"id":"Qwen/Qwen3-0.6B","object":"model","created":1762912492,"owned_by":"sglang","root":"Qwen/Qwen3-0.6B","max_model_len":40960}]}

% curl http://dgx1:8000/v1/models
{"object":"list","data":[{"id":"Qwen/Qwen3-0.6B","object":"model","created":1762913773,"owned_by":"vllm","root":"Qwen/Qwen3-0.6B","parent":null,"max_model_len":40960,"permission":[{"id":"modelperm-738dc17a0b4945108767d7aa84bab062","object":"model_permission","created":1762913773,"allow_create_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"organization":"*","group":null,"is_blocking":false}]}]}

% curl http://dgx2:8000/v1/models
{"object":"list","data":[{"id":"Qwen/Qwen3-0.6B","object":"model","created":1762913826,"owned_by":"vllm","root":"Qwen/Qwen3-0.6B","parent":null,"max_model_len":40960,"permission":[{"id":"modelperm-ab40829c262944c39305bffacc508ff6","object":"model_permission","created":1762913826,"allow_create_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"organization":"*","group":null,"is_blocking":false}]}]}
```


### jupyterlab

*Error가 있어 사용이 어려 움. vscode or cursor의 remote-ssh를 사용하세요.*

1. Spark 장치에 SSH-ing하여 할당된 JupyterLab 포트를 확인하고 다음 명령을 실행하십시오.
```sh
cat /opt/nvidia/dgx-dashboard-service/jupyterlab_ports.yaml
```
2. 사용자 이름을 찾고 할당된 포트 번호를 기록해 두세요
3. pc에서 두 포트를 모두 포함하는 새 SSH 터널을 만듭니다.
```sh
ssh -L 11000:localhost:11000 -L 11002:localhost:11002 didimai@211.218.150.245 -p 50024

ssh -L 11000:localhost:11000 -L 11002:localhost:11002 didimai@211.218.150.246 -p 50024
```
4. 웹 브라우저를 열고 `http://localhost:11000`으로 이동합니다.