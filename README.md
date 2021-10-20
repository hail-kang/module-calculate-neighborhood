# Module-calculate-neighborhood
데이터간의 유사도 분석 및 추천 모델 개발

# 필요 모듈
- numpy

# 필요 모듈 설치
```text
pip install numpy
```

# 사용 방법
```python
# Cosine유사도를 이용한 코드

from neighborhood import *

s = CosineSimilarity({'a': 2, 'b': 1, 'c': 5})
n = Neighborhood(s, 0.5)
r = RatioRecommend(n)
r.add({'a': 2, 'b': 1, 'c': 5, 'd': 4})
r.add({'a': 3, 'b': 1, 'c': 5, 'd': 4})
r.add({'a': 2, 'b': 2, 'c': 5, 'd': 3})
p = r.report(3, 0.5)
print(p)
```
