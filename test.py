from neighborhood import *

s = CosineSimilarity({'a': 2, 'b': 1, 'c': 5})
n = Neighborhood(s, 0.5)
r = RatioRecommend(n, 3)
r.add({'a': 2, 'b': 1, 'c': 5, 'd': 4})
r.add({'a': 3, 'b': 1, 'c': 5, 'd': 4})
r.add({'a': 2, 'b': 2, 'c': 5, 'd': 3})
p = r.report(0.5)
print(p)