import unittest

from neighborhood import *

class RecommendTest(unittest.TestCase):

  def test_cosine_smallcase(self):
    print('=====test_cosine_smallcase=====')
    s = CosineSimilarity({'a': 2, 'b': 1, 'c': 5})
    n = Neighborhood(s, 0.5)
    r = RatioRecommend(n)
    r.add({'a': 2, 'b': 1, 'c': 5, 'd': 4})
    r.add({'a': 3, 'b': 1, 'c': 5, 'd': 4})
    r.add({'a': 2, 'b': 2, 'c': 5, 'd': 3})
    p = r.report(3, 0.5)
    print(p)
    print('==============end=============')

  def test_cosine_randomcase(self):
    print('=====test_cosine_randomcase=====')
    import random

    for i in range(2000):
      a = dict()
      count = random.randint(1, 26)
      for j in random.sample(range(26), count):
          key = chr(ord('a') + j)
          value = random.randint(1, 5)
          a[key] = value
      if i == 0:
        s = CosineSimilarity(a)
        n = Neighborhood(s, 0.5)
        r = RatioRecommend(n)
      else:
        r.add(a)
    p = r.report(3, 0.5)

    print(s.origin)
    for nei in n.neighborhoods:
      print(nei)
    print(p)
    print('==============end=============')

if __name__ == '__main__':
  unittest.main()