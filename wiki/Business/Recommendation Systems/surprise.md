---
title: surprise
related_raw:
  - "[[wiki/Business/Recommendation Systems/surprise]]"
tags:
  - wiki
  - knowledge_and_memory
  - recommendation_systems
type: wiki
status: draft
last_updated: "2026-04-19"
updated: "2026-04-19"
---

**개요**

Surprise는 추천 시스템을 구축하고 분석하기 위한 파이썬 라이브러리입니다. 이 라이브러리는 사용자에게 개인화된 추천 목록을 제공하는 시스템을 설계하는 데 사용됩니다. Surprise는 특히 평가 예측을 위한 알고리즘을 제공하며, scikit-learn API를 따르기 때문에 파이썬 기계 학습 생태계에 익숙한 사용자에게 친숙합니다.

**주요 기능**

• **평가 예측 알고리즘**: Surprise는 SVD, NMF와 같은 행렬 분해 기반 알고리즘 및 유사성 기반 알고리즘을 포함한 다양한 평가 예측 알고리즘을 제공합니다.
• **모델 평가 및 선택**: 교차 검증(iterators)과 내장된 메트릭스를 통해 모델 평가를 지원하며, 하이퍼파라미터 검색을 위한 그리드 검색 및 랜덤 검색 도구도 제공합니다.
• **데이터셋 지원**: MovieLens와 같은 클래식 데이터셋을 포함하며, CSV 파일 로드 및 pandas 데이터프레임을 통한 사용자 정의 데이터셋도 지원합니다.
• **성능 최적화**: Cython을 사용하여 계산 집약적인 부분을 최적화하고, 내부적으로 Python의 기본 데이터 구조와 numpy 배열을 사용합니다.

**예제 코드**

다음은 MovieLens 데이터셋을 로드하고 SVD 알고리즘을 사용하여 5-fold 교차 검증을 수행하는 간단한 예제입니다:
```python
from surprise import SVD, Dataset
from surprise.model_selection import cross_validate

# 내장된 MovieLens 100k 데이터셋 로드
data = Dataset.load_builtin('ml-100k')

# SVD 알고리즘 사용
algo = SVD()

# 5-fold 교차 검증 수행 및 결과 출력
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
```

이 코드는 SVD 알고리즘을 사용하여 각 폴드의 RMSE와 MAE를 계산하고, 평균 및 표준 편차를 출력합니다.

---
### 관련 노트
- SVD 알고리즘
- 구현체