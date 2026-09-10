---
title: "MCP 기능"
related_raw: ["[[wiki/Agents/Frameworks/MCP/MCP 기능.md]]"]
tags: ['wiki', 'agents_and_systems', 'text-to-sql_(t2sql)_&_analytics']
type: "wiki"
status: "published"
last_updated: "2026-04-19"
updated: "2026-04-19"
---

### SQL 데이터베이스 기능 함수

🔍 스키마 및 데이터 조회
• find_tables_by_keyword(keyword): 키워드와 관련된 테이블 목록을 찾아줍니다.
• get_schema(table_name): 특정 테이블의 컬럼 이름과 데이터 타입을 조회합니다.
• get_table_description(table_name): 테이블에 대한 주석을 조회해 어떤 데이터를 담고 있는지 파악합니다.
• find_value_mapping(keyword): 키워드와 관련된 코드화된 값(예: 1, 2, 3)의 의미와 사용된 컬럼목록을 찾아 줍니다. 
• get_sample_data(table_name, conditions=null,  limit=10): 테이블의 샘플 데이터를 확인하여 데이터 구조와 내용을 파악합니다.
• check_value_mapping(table_name, column_name): 특정 컬럼의 코드화된 값(예: 1, 2, 3)의 의미를 확인합니다
• get_keys(table_name): 테이블의 기본 키(PK)와 고유 키(UK) 정보를 조회합니다.
• get_indexes(table_name): 테이블에 정의된 인덱스 목록을 조회합니다.
• analyze_sql_plan(sql_query): 쿼리의 실행 계획을 분석하여 성능 병목 지점을 파악합니다.

🚀 쿼리 생성
• write_sql_query(user_question, domain=null): 사용자의 질문(user_question)을 분석하여 SQL 쿼리를 생성합니다. 이 함수는 필요한 테이블과 컬럼, 조건을 자동으로 식별합니다.
• optimize_sql_query(sql_query, user_question): 생성된 쿼리를 최적화하고, 원래의 사용자 질문(user_question)을 참고하여 더 효율적인 쿼리를 제안합니다. 이 과정에서 인덱스, 조인 방식 등을 고려합니다.

### 동작 원리

write_sql_query(user_question, domain) 함수는 다음 단계를 거쳐 SQL 쿼리를 생성합니다.
1. 질문 분석: 사용자 질문(user_question)에서 핵심 키워드, 테이블 이름, 컬럼, 그리고 조건을 파악합니다. 예를 들어 "서울에 사는 남학생들의 이름과 나이를 알려줘"라는 질문에서 '서울'과 '남학생'은 조건, '이름'과 '나이'는 컬럼, '학생'은 테이블 이름과 관련이 있음을 분석합니다.
2. 테이블 및 스키마 매핑: 분석된 키워드를 기반으로 어떤 테이블과 컬럼을 사용해야 하는지 데이터베이스의 스키마 정보를 통해 매핑합니다. 이 과정에서 find_tables_by_keyword()와 get_schema() 같은 다른 함수들의 도움을 받을 수 있습니다.
3. 쿼리 구성: 분석된 정보(테이블, 컬럼, 조건)를 바탕으로 SELECT, FROM, WHERE 절 등을 조합하여 완전한 SQL 쿼리 문장을 만듭니다. 이 과정에서 check_value_mapping() 함수를 사용하여 '남학생' 같은 의미를 데이터베이스의 실제 값(예: '1')으로 변환할 수 있습니다.
4. 쿼리 반환: 최종적으로 생성된 SQL 쿼리 문자열을 반환합니다.

optimize_sql_query(sql_query, user_question) 함수는 다음 단계를 거쳐 SQL 쿼리를 최적화합니다.
1. 실행 계획 분석: 먼저 analyze_sql_plan(sql_query) 함수를 호출하여 현재 쿼리의 실행 계획을 분석합니다. 이 과정에서 Full Table Scan과 같은 비효율적인 연산이 있는지, JOIN 순서가 적절한지, 어떤 인덱스가 사용되었는지 등을 파악합니다.
2. 문제점 식별: 실행 계획 분석 결과를 바탕으로 쿼리의 문제점을 식별합니다. 예를 들어, 대량의 데이터에 대해 ORDER BY 연산이 일어나거나, JOIN에 사용된 컬럼에 인덱스가 없어 느리게 동작하는 경우 등을 찾아냅니다.
3. 최적화 전략 수립: 식별된 문제점에 따라 최적화 전략을 세웁니다.
	• 인덱스 활용: WHERE 절이나 JOIN 조건에 인덱스를 추가하거나, 기존 인덱스를 더 효율적으로 활용하도록 쿼리를 수정합니다.
	• 컬럼 최적화: SELECT * 대신 필요한 컬럼만 명시하여 데이터 전송량을 줄입니다.
	• JOIN 방식 변경: Nested Loop Join 대신 Hash Join이나 Merge Join이 더 효율적일 경우 쿼리 힌트(hint)를 사용하여 방식을 변경하도록 제안합니다.
	• 서브쿼리 최적화: IN을 EXISTS로 바꾸는 등 서브쿼리 구조를 개선합니다.
4. 최적화된 쿼리 생성 및 제안: 수립된 전략을 바탕으로 새로운, 더 효율적인 SQL 쿼리 문장을 생성하여 사용자에게 제안합니다. 이 과정에서 원래의 질문(user_question)을 참고하여 사용자의 의도에 부합하는지 다시 한번 확인합니다.