import abc
import numbers

from numpy import dot
from numpy.linalg import norm

class Similarity(metaclass=abc.ABCMeta):

  @abc.abstractclassmethod
  def distance(self):
    pass

  @abc.abstractclassmethod
  def keys(self):
    pass

  @abc.abstractclassmethod
  def values(self):
    pass

  @abc.abstractclassmethod
  def report(self):
    pass

class CosineSimilarity(Similarity):

  def __init__(self, origin:dict):
    if not isinstance(origin, dict):
      raise Exception('origin must be dict')
    elif not all(map(lambda x : isinstance(x, numbers.Number), origin.values())):
      raise Exception('value of origin must be number')
    self.origin = origin

    self.__origin_keys = set(self.keys())
    self.__other_keys = None
    self.__origin_values = None
    self.__other_values = None

  def keys(self) -> iter:
    return self.origin.keys()

  def values(self) -> iter:
    return self.origin.values()

  def distance(self, other) -> float:
    self.__other_keys = set(other.keys())
    union_keys = self.__origin_keys | self.__other_keys
    self.__origin_values = [self.origin[key] if key in self.__origin_keys else 0 for key in union_keys]
    self.__other_values = [other[key] if key in self.__other_keys else 0 for key in union_keys]

    d = (norm(self.__origin_values)*norm(self.__other_values))
    if d == 0:
      return 0
    return dot(self.__origin_values, self.__other_values)/d

  def report(self, other) -> dict:
    distance = self.distance(other)
    substract_keys = self.__other_keys - self.__origin_keys
    return {
      'distance': distance,
      'key_value': { key: other[key] for key in substract_keys }
    }
