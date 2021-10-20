import unittest

from neighborhood import *

class RecommendTest(unittest.TestCase):

  def test_cosine_smallcase(self):
    s = CosineSimilarity({'a': 2, 'b': 1, 'c': 5})
    n = Neighborhood(s, 0.5)
    r = RatioRecommend(n)
    r.add({'a': 2, 'b': 1, 'c': 5, 'd': 4})
    r.add({'a': 3, 'b': 1, 'c': 5, 'd': 4})
    r.add({'a': 2, 'b': 2, 'c': 5, 'd': 3})
    p = r.report(3, 0.5)
    print(p)

if __name__ == '__main__':
  unittest.main()