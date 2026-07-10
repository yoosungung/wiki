---
title: "Airflow DAG 테스트 환경 구축"
related_raw: ["[[wiki/Engineering/Infrastructure-and-DevOps/Airflow DAG 테스트 환경 구축.md]]"]
tags: ['wiki', 'engineering_and_infra', 'dev_environment', 'infrastructure_orchestration']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
---

## local run airflow

1. sqlite3 init
```bash
airflow db init
```

2. local run
```bash
airflow webserver -p 8080
airflow scheduler
```

3. dag editing

4. dag reload
```bash
airflow dags reserialize
```