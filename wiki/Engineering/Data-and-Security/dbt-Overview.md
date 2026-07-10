# dbt (data build tool) 개요

dbt(data build tool)는 현대 데이터 스택(Modern Data Stack)에서 데이터 변환(Transformation)을 담당하는 오픈소스 도구입니다. ELT(Extract, Load, Transform) 파이프라인에서 'T'에 집중하여, SQL을 이용해 효율적이고 안정적인 데이터 변환을 수행할 수 있게 돕습니다.

## 1. 탄생 배경 및 ELT 패러다임
과거의 ETL(Extract, Transform, Load) 방식과 달리, 최근에는 클라우드 데이터 웨어하우스(Snowflake, BigQuery 등)의 강력한 성능을 활용하여 데이터를 먼저 적재하고 내부에서 변환하는 **ELT** 방식이 주류가 되었습니다. dbt는 이러한 ELT 구조에서 데이터 변환 로직을 관리하는 최적의 도구입니다.

## 2. 핵심 작동 방식
dbt는 원본 데이터를 추출하거나 직접 적재하지 않습니다. 대신, DW 내에 있는 원본 데이터를 바탕으로 `SELECT` 쿼리를 작성하면, dbt가 이를 테이블(Table)이나 뷰(View)로 구체화(Materialization)해 줍니다. 사용자는 비즈니스 로직 정의에만 집중하고, 복잡한 DDL(Data Definition Language) 생성은 dbt에 맡깁니다.

## 3. 주요 기능 및 장점 (Software Engineering Best Practices)
dbt는 데이터 분석 영역에 소프트웨어 공학의 방법론을 도입했습니다.

- **Jinja 템플릿**: SQL 내부에서 변수, 조건문, 반복문을 사용하여 동적 쿼리를 작성하고 코드를 재사용(매크로)할 수 있습니다.
- **버전 관리 (Git)**: 데이터 파이프라인 코드를 Git으로 관리하여 변경 이력을 추적하고 협업할 수 있습니다.
- **데이터 계보(Lineage)**: 모델 간의 의존 관계를 자동으로 파악하여 DAG(Directed Acyclic Graph) 형태의 시각적 계보와 문서를 제공합니다.
- **데이터 품질 테스트**: Null 체크, Unique 체크 등 데이터 무결성을 검증하는 테스트를 자동화할 수 있습니다.
- **환경 분리**: 개발(Dev)과 운영(Prod) 환경을 쉽게 분리하여 안전한 배포가 가능합니다.

## 4. 시맨틱 레이어(Semantic Layer)와 AI 에이전트
dbt는 단순한 변환 도구를 넘어 **시맨틱 레이어**로서의 역할을 강화하고 있습니다.

- **MetricFlow**: 비즈니스 지표(예: 매출, 이탈률)를 코드 기반으로 중앙에서 정의하여 데이터 일관성을 유지합니다.
- **Text-to-SQL 에이전트 연동**: AI가 복잡한 SQL을 직접 생성하는 대신, dbt에 정의된 표준화된 메트릭을 호출하게 함으로써 **정확도를 획기적으로 향상**(최대 300%)시킬 수 있습니다.
- **OSI (Open Semantic Interchange)**: dbt Labs는 업계 표준 시맨틱 규격인 OSI v1.0을 주도하며 생태계를 확장하고 있습니다.

## 5. KM 프로젝트 내 관련 링크
- [[wiki/Engineering/Data-and-Security/OSI-Open-Semantic-Interchange|OSI (Open Semantic Interchange)]]
- [[wiki/Agents/Text-to-SQL/2026-04-22-T2SQL-Trends-Update|T2SQL Trends (Databao Agent & dbt)]]
- [[wiki/Engineering/Data-and-Security/Semantic-Layer-Spec|시맨틱 레이어 스펙]]

## 참고 자료
- [dbt Official Documentation](https://docs.getdbt.com/)
- [dbt Labs GitHub](https://github.com/dbt-labs/dbt-core)
