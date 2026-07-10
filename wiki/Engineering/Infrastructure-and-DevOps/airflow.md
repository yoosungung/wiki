---
title: "airflow"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/airflow.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'infrastructure_orchestration']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

Airflow에서 DAG를 비정기적/정기적으로 수행할 때 arguments를 전달하는 방법은 DagRun 객체와 trigger_dag 함수를 활용하는 것입니다.

**1. 정기적 수행**
정기적으로 DAG를 실행할 경우, DAG 정의에서 기본적인 default_args나 params를 통해 전달할 수 있습니다. 예를 들어, params를 사용하여 기본 인자를 설정할 수 있습니다:
```python
from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'params': {'my_param': 'default_value'},
}

with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    _# Task 정의_
    pass
```
이 경우, my_param은 모든 실행에 대해 기본값을 가집니다.

**2. 비정기적 수행**
DAG를 비정기적으로 실행할 때, trigger_dag와 conf 파라미터를 사용하여 인자를 전달할 수 있습니다. 예를 들어, trigger_dag를 호출하여 conf 파라미터를 통해 인자를 전달하는 방법입니다:
```python
from airflow.api.client.local import Client

client = Client(api_base_url='http://localhost:8080')

response = client.trigger_dag(
    dag_id='my_dag',
    conf={'my_param': 'custom_value'}
)

dag_run_id = response['dag_run_id']
print(f"DAG {dag_id} triggered with dag_run_id: {dag_run_id}")
```
conf로 전달된 값은 DAG의 실행 시점에서 dag_run.conf로 접근할 수 있습니다.

**3. DAG 내에서 인자 사용**
DAG 내에서 dag_run.conf로 전달된 인자는 각 Task 내에서 PythonOperator 등을 통해 사용할 수 있습니다:
```python
def my_function(**kwargs):
    param = kwargs['dag_run'].conf.get('my_param', 'default_value')
    print(f"Received parameter: {param}")

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:
    task = PythonOperator(
        task_id='my_task',
        python_callable=my_function,
        provide_context=True
    )
```
이렇게 설정하면 비정기적으로 DAG를 실행할 때마다 인자를 전달하고 이를 사용할 수 있습니다.

**4. DAG 상태 추적하기**
DAG가 실행되면, 상태를 주기적으로 확인하면서 실행이 완료되었는지 추적할 수 있습니다. get_dag_run을 사용하여 해당 DAG의 상태를 조회할 수 있습니다.
```python
# DAG 상태 추적
while True:
    # dag_run 상태 조회
    dag_run = client.get_dag_run(dag_id=dag_id, dag_run_id=dag_run_id)
    
    state = dag_run['state']
    print(f"DAG Run {dag_run_id} 상태: {state}")
    
    # 실행 상태가 'success' 또는 'failed'이면 종료
    if state in ['success', 'failed']:
        break
    
    # 10초마다 상태 체크
    time.sleep(10)

print(f"DAG {dag_id} 실행 완료 - 최종 상태: {state}")
```

---
### KubernetesPodOperator 사용

Airflow에서 Kubernetes를 사용하여 동적으로 작업을 실행하는 방법에 대한 자세한 내용은 [[wiki/Engineering/Infrastructure-and-DevOps/KuberbetesPodOperator]] 노트를 참고하세요.

---
### 최신 업데이트: Airflow Common AI Provider
2026년에 출시된 **Common AI Provider**를 통해 LLM 및 AI 에이전트를 DAG에 직접 통합하는 방법에 대해서는 [[wiki/Engineering/Infrastructure-and-DevOps/Airflow-Common-AI-Provider.md]] 문서를 확인하세요.