---
title: "KuberbetesPodOperator"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/KuberbetesPodOperator.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'infrastructure_orchestration']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

**0. fine_tune.py 스크립트에서 인자 처리**
Docker 이미지에 포함된 fine_tune.py 스크립트에서는 전달된 인자를 파싱하여 S3에서 데이터셋과 모델을 로드하고, 파인 튜닝 작업을 수행한 후, 결과를 S3에 저장하도록 구현해야 합니다.
```python
import sys
import boto3

def main():
    dataset_path = sys.argv[1]
    model_path = sys.argv[2]
    # S3에서 데이터셋과 모델 로드
    s3 = boto3.client('s3')
    # 데이터셋 및 모델 로드 로직 구현
    # ...
    # 파인 튜닝 작업 수행
    # ...
    # 결과 모델을 S3에 저장
    # ...
if __name__ == '__main__':
    main()
```

**1. Docker 이미지 준비**
먼저, 파인 튜닝 코드를 포함한 Docker 이미지를 준비해야 합니다. 이 이미지에는 필요한 라이브러리와 S3에 접근하기 위한 AWS 자격 증명이 포함되어야 합니다. 아래는 Dockerfile의 예시입니다:
```dockerfile
FROM python:3.10-slim
# 필수 패키지 설치
RUN pip install torch transformers boto3
# 작업 디렉토리 설정
WORKDIR /app
# 파인 튜닝 스크립트 추가
COPY fine_tune.py .
# 엔트리포인트 설정
ENTRYPOINT ["python", "fine_tune.py"]
```
fine_tune.py 스크립트는 S3에서 데이터셋과 모델을 로드하고, 파인 튜닝을 수행한 후, 결과 모델을 S3에 저장하는 로직을 포함해야 합니다. 예를 들어, boto3 라이브러리를 사용하여 S3와 상호작용할 수 있습니다.

**2. AWS 자격 증명 설정**
S3에 접근하기 위해 AWS 자격 증명이 필요합니다. 이는 Kubernetes의 Secret을 통해 설정할 수 있습니다. 먼저, AWS 자격 증명을 포함한 Secret을 생성합니다:
```bash
kubectl create secret generic aws-secret --from-literal=AWS_ACCESS_KEY_ID=your_access_key_id --from-literal=AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

**3. 필요한 패키지를 설치해야 합니다.**
```bash
pip install apache-airflow[cncf.kubernetes]
```

**4. Airflow DAG 설정**
Airflow에서 KubernetesPodOperator를 사용하여 파인 튜닝 작업을 정의합니다:
```python
import datetime
from airflow import DAG
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

default_args = {
    'start_date': datetime(2024, 12, 29),
}

# 리소스 요구 사항 설정
resources = k8s.V1ResourceRequirements(
    limits={"memory": "4Gi", "cpu": "2"},
    requests={"memory": "2Gi", "cpu": "1"},
)

# AWS 자격 증명을 환경 변수로 설정
env_vars = [
    k8s.V1EnvVar(
        name="AWS_ACCESS_KEY_ID",
        value_from=k8s.V1EnvVarSource(
            secret_key_ref=k8s.V1SecretKeySelector(
                name="aws-secret",
                key="AWS_ACCESS_KEY_ID"
            )
        )
    ),
    k8s.V1EnvVar(
        name="AWS_SECRET_ACCESS_KEY",
        value_from=k8s.V1EnvVarSource(
            secret_key_ref=k8s.V1SecretKeySelector(
                name="aws-secret",
                key="AWS_SECRET_ACCESS_KEY"
            )
        )
    ),
]

# DAG 정의
with DAG(
    'fine_tuning_model',
    default_args=default_args,
    schedule_interval=None,
    params={
        'dataset_path': 's3://your-bucket/dataset',
        'model_path': 's3://your-bucket/model',
    },
    catchup=False,
) as dag:
    # KubernetesPodOperator 정의
    fine_tune_task = KubernetesPodOperator(
	    task_id='fine_tune_model',
	    name='fine_tune_model_pod',
	    namespace='default',
	    image='your_docker_image:latest',
	    cmds=['python', 'fine_tune.py'],
	    arguments=[
	        '{{ params.dataset_path }}',
	        '{{ params.model_path }}',
	    ],
	    env_vars=env_vars,
	    is_delete_operator_pod=True,
	    get_logs=True,
	    resources=resources,
    )
```

**4. S3 버킷 및 권한 설정**
S3 버킷을 생성하고, 해당 버킷에 대한 읽기/쓰기를 허용하는 IAM 정책을 설정해야 합니다. 이러한 설정은 AWS 관리 콘솔을 통해 수행할 수 있습니다.

**5. 파라메터로 호출**
Airflow UI나 CLI를 통해 DAG을 트리거할 때 파라미터를 전달할 수 있습니다. 예를 들어, Airflow UI에서 DAG을 수동으로 트리거할 때 `Trigger DAG w/ config` 옵션을 사용하여 JSON 형식으로 파라미터를 입력할 수 있습니다.
```json
{
    "dataset_path": "s3://your-bucket/new-dataset",
    "model_path": "s3://your-bucket/new-model"
}
```
또는 CLI를 통해 DAG을 트리거할 때 --conf 옵션을 사용하여 파라미터를 전달할 수 있습니다:
```bash
airflow dags trigger --conf '{"dataset_path":"s3://your-bucket/new-dataset", "model_path":"s3://your-bucket/new-model"}' fine_tuning_model
```