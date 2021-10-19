from neighborhood import recommend, similarity, neighborhood

s = similarity.CosineSimilarity({'a': 2, 'b': 1, 'c': 5})
n = neighborhood.Neighborhood(s, 0.5)
r = recommend.RatioRecommend(n, 3)
r.add({'a': 2, 'b': 1, 'c': 5, 'd': 4})
p = r.report(0.7)
print(p)