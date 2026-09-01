RTX 4090 2장을 활용하여 `Qwen2.5-Coder-32B-Instruct (Q4_K_M)` 모델을 k3s 및 vLLM 기반으로 서빙하고, Continue.dev와 연동하는 폐쇄망 환경 구축 상세 계획입니다.

## 1. 검증된 소프트웨어 호환성 매트릭스 (Recommended Version Matrix)

폐쇄망 환경 구축 시 라이브러리 간 버전 불일치로 인한 Build/CUDA Mismatch 오류를 방지하기 위해 **검증된 조합**을 사용해야 합니다.

| 구분                   | 추천 소프트웨어 / 구성요소                | 검증 버전                                  | 비고                                    |
| -------------------- | ------------------------------ | -------------------------------------- | ------------------------------------- |
| **OS**               | Ubuntu Linux                   | **22.04.4 LTS** (Kernel 5.15 / 6.5)    | 엔터프라이즈 GPU 드라이버 호환성 최적                |
| **GPU Driver**       | NVIDIA Linux Driver            | **550.54.14** (or 550.x Production)    | CUDA 12.4 지원 및 Ada Lovelace(4090) 안정화 |
| **CUDA Toolkit**     | NVIDIA CUDA                    | **12.4.1**                             | vLLM 0.6.x+ 컴파일 바이너리 호환               |
| **Container Engine** | Containerd / Container Toolkit | **NVIDIA Container Toolkit v1.15.0**   | k3s 연동 GPU Passthrough 핵심             |
| **Kubernetes**       | k3s (Rancher Lightweight K8s)  | **v1.29.4+k3s1** 또는 **v1.30.2+k3s1**   | 경량화 K8s, 폐쇄망 단일 노드 구축 최적              |
| **Inference Engine** | vLLM                           | **v0.6.3** (`vllm/vllm-openai:v0.6.3`) | GGUF/AWQ 지원 및 Tensor Parallelism 지원   |
| **LLM Weights**      | Qwen2.5-Coder-32B-Instruct     | **GGUF (Q4_K_M)** 또는 **AWQ 4-bit**     | AWQ 사용 시 vLLM 추론 속도 대폭 상승             |
| **IDE Plugin**       | Continue.dev                   | **v0.8.x 이상**                          | VS Code / JetBrains 최신 확장             |

## 2. 하드웨어 리소스 및 VRAM 구조 설계

- **GPU 구성:** NVIDIA RTX 4090 24GB x 2EA (총 48GB VRAM)
- **병렬 처리 (Tensor Parallelism):** `--tensor-parallel-size 2` 설정
- **VRAM 분배 계산:**
    - `Qwen2.5-Coder-32B (Q4_K_M)` 모델 가중치: 약 19.5GB~20GB
    - **GPU당 가중치 점유:** 카드당 약 10GB씩 분할 로드
    - **여유 VRAM (KV Cache 전용):** 카드당 약 13GB~14GB 확보
    - **지원 컨텍스트 길이너비:** 최대 **32,768 (32K) 토큰**까지 OOM(Out of Memory) 없이 동시 처리 가능.

## 3. 단계별 구축 프로세스 (Step-by-Step Implementation)

### [Step 1] 호스트 OS 및 NVIDIA GPU 환경 준비 (Air-Gapped)

1. **NVIDIA 드라이버 설치 (Ubuntu 22.04):** 외부망에서 다운로드한 `.run` 파일 또는 오프라인 deb 패키지를 이관하여 설치합니다.
    ```bash
    sudo apt-get update && sudo apt-get install -y build-essential gcc
    sudo sh NVIDIA-Linux-x86_64-550.54.14.run --silent --dkms
    nvidia-smi  # 2장의 RTX 4090 인식 및 드라이버 버전 확인
    ```
    
2. **NVIDIA Container Toolkit 설치 및 설정:** `containerd`가 GPU를 인지할 수 있도록 런타임을 등록합니다.
    ```bash
    # 오프라인 패키지(nvidia-container-toolkit) 설치 후
    sudo nvidia-ctk runtime configure --runtime=containerd
    sudo systemctl restart containerd
    ```

### [Step 2] k3s 설치 및 GPU 런타임 연동

1. **k3s 오프라인 설치:** k3s 바이너리와 에어갭 이미지 타르볼(`k3s-airgap-images-amd64.tar.zst`)을 `/var/lib/rancher/k3s/agent/images/` 디렉토리에 배치한 후 설치합니다.
    ```bash
    INSTALL_K3S_SKIP_DOWNLOAD=true ./install.sh
    ```
    
2. **k3s containerd에 NVIDIA Runtime 등록:** `/etc/rancher/k3s/config.yaml.d/nvidia.yaml` 설정 추가 또는 `/var/lib/rancher/k3s/agent/etc/containerd/config.toml.tmpl`을 작성하여 `nvidia-container-runtime`을 기본/선택 런타임으로 지정합니다.
    ```toml
    # /var/lib/rancher/k3s/agent/etc/containerd/config.toml.tmpl 예시
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia]
      runtime_type = "io.containerd.runc.v1"
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia.options]
        BinaryName = "/usr/bin/nvidia-container-runtime"
    ```
    
    ```bash
    sudo systemctl restart k3s
    ```

### [Step 3] vLLM 배포를 위한 K8s Manifest 작성 및 배포

외부에서 다운로드한 `qwen2.5-coder-32b-instruct-q4_k_m.gguf` 파일(또는 AWQ 가중치 폴더)을 서버의 `/data/models/` 경로에 배치합니다.

1. **PersistentVolume(PV) 및 PVC 생성 (`model-pv.yaml`):**
    ```yaml
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: model-pv
    spec:
      capacity:
        storage: 50Gi
      accessModes:
        - ReadOnlyMany
      persistentVolumeReclaimPolicy: Retain
      hostPath:
        path: /data/models
    ---
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: model-pvc
      namespace: default
    spec:
      accessModes:
        - ReadOnlyMany
      resources:
        requests:
          storage: 50Gi
    ```
    
2. **vLLM Deployment 작성 (`vllm-deployment.yaml`):** `--tensor-parallel-size 2` 옵션을 지정하여 GPU 2장을 병렬 활용하도록 설정합니다.
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: vllm-qwen-coder
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: vllm-qwen-coder
      template:
        metadata:
          labels:
            app: vllm-qwen-coder
        spec:
          containers:
          - name: vllm-container
            image: vllm/vllm-openai:v0.6.3
            imagePullPolicy: IFNotPresent
            command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
            args:
              - "--model"
              - "/model/qwen2.5-coder-32b-instruct-q4_k_m.gguf"
              - "--tensor-parallel-size"
              - "2"
              - "--max-model-len"
              - "32768"
              - "--gpu-memory-utilization"
              - "0.90"
              - "--port"
              - "8000"
              - "--served-model-name"
              - "qwen2.5-coder-32b"
            resources:
              limits:
                nvidia.com/gpu: "2"
              requests:
                nvidia.com/gpu: "2"
            ports:
              - containerPort: 8000
            volumeMounts:
              - name: model-volume
                mountPath: /model
          volumes:
            - name: model-volume
              persistentVolumeClaim:
                claimName: model-pvc
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: vllm-service
      namespace: default
    spec:
      type: NodePort
      selector:
        app: vllm-qwen-coder
      ports:
        - port: 8000
          targetPort: 8000
          nodePort: 30800
    ```
    
3. **배포 및 상태 확인:**
    ```bash
    kubectl apply -f model-pv.yaml
    kubectl apply -f vllm-deployment.yaml
    kubectl get pods -w
    # vLLM 로그 확인 (가중치 로딩 및 GPU 2장 인식 확인)
    kubectl logs -f deployment/vllm-qwen-coder
    ```

### [Step 4] Continue.dev 확장 프로그램 설정 (개발자 단말)

개발자의 VS Code 또는 JetBrains IDE에 설치된 Continue.dev의 `config.json` (위치: `~/.continue/config.json`)을 다음과 같이 편집합니다.
```json
{
  "models": [
    {
      "title": "Qwen2.5-Coder-32B (Chat/Edit)",
      "provider": "openai",
      "model": "qwen2.5-coder-32b",
      "apiBase": "http://<k3s-node-ip>:30800/v1",
      "apiKey": "EMPTY",
      "completionOptions": {
        "temperature": 0.2,
        "maxTokens": 2048
      }
    }
  ],
  "tabAutocompleteModel": {
    "title": "Qwen2.5-Coder-32B (Autocomplete)",
    "provider": "openai",
    "model": "qwen2.5-coder-32b",
    "apiBase": "http://<k3s-node-ip>:30800/v1",
    "apiKey": "EMPTY"
  },
  "allowAnonymousTelemetry": false
}
```

## 4. 트러블슈팅 및 폐쇄망 운영 유의사항

1. **Fill-In-the-Middle (FIM) 자동완성 깨짐 현상 방지:** `Qwen2.5-Coder` 계열 모델을 vLLM 백엔드로 자동완성에 연결할 때, 스톱 토큰 매핑 문제로 무한 루프 코드가 생성될 수 있습니다. vLLM 실행 명령에 `--stop-token`매개변수로 `<|cursor|>` 및 `<|endoftext|>`가 인지되고 있는지 확인해야 합니다.
2. **vLLM 모델 포맷 추천 (GGUF vs AWQ):** vLLM 환경에서는 GGUF보다 **AWQ(Activation-aware Weight Quantization)** 양자화 모델(`Qwen2.5-Coder-32B-Instruct-AWQ`)을 사용할 때 GPU 연산 커널 최적화가 더 뛰어나 약 20~30% 더 높은 초당 토큰 생성 속도(Tokens/sec)를 확보할 수 있습니다. GGUF 로드 시 병목이 발생하면 AWQ 포맷 전환을 권장합니다.
3. **외부 텔레메트리 완전 차단:** Continue.dev 및 VS Code 확장이 내부망 외부로 네트워크 통신을 시도하지 않도록 `allowAnonymousTelemetry: false` 설정을 `config.json`에 반영해야 합니다.