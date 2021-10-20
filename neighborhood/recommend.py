import abc

from .neighborhood import Neighborhood

class Recommend(metaclass=abc.ABCMeta):
  
  def __init__(self, neighborhood):
    if not isinstance(neighborhood, Neighborhood):
      raise Exception('neighborhood must be Neighborhood')
    self.neighborhood = neighborhood

  def add(self, other):
    self.neighborhood.add(other)

  @abc.abstractclassmethod
  def report(self):
    pass

class RatioRecommend(Recommend):

  def report(self, score_standard, ratio_standard):
    count = dict()
    report = self.neighborhood.report()
    for data in report:
      for key in data['key_value']:
        if not key in count:
          count[key] = {
            'total_count': 0,
            'effect_count': 0
          }

        count[key]['total_count'] += 1
        if data['key_value'][key] > score_standard:
          count[key]['effect_count'] += 1

    return { key: {**count[key], 'ratio': count[key]['effect_count']/count[key]['total_count']}\
       for key in filter(lambda x: count[x]['effect_count']/count[x]['total_count'] > ratio_standard, count.keys()) }
