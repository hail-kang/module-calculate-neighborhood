import abc
import numbers

from numpy import dot
from numpy.linalg import norm

class Similarity(metaclass=abc.ABCMeta):

  def __init__(self, origin:dict):
    if not isinstance(origin, dict):
      raise Exception('origin must be dict')
    elif not all(map(lambda x : isinstance(x, numbers.Number), origin.values())):
      raise Exception('value of origin must be number')
    self.origin = origin

    self._origin_keys = set(self.keys())
    self._other_keys = None
    self._origin_values = None
    self._other_values = None

  def keys(self) -> iter:
    return self.origin.keys()

  def values(self) -> iter:
    return self.origin.values()

  def report(self, other) -> dict:
    distance = self.distance(other)
    substract_keys = self._other_keys - self._origin_keys
    return {
      'distance': distance,
      'key_value': { key: other[key] for key in substract_keys }
    }
  
  @abc.abstractclassmethod
  def distance(self):
    pass

class CosineSimilarity(Similarity):
    
  def distance(self, other) -> float:
    self._other_keys = set(other.keys())
    # union_keys = self._origin_keys | self._other_keys
    # self._origin_values = [self.origin[key] if key in self._origin_keys else 0 for key in union_keys]
    # self._other_values = [other[key] if key in self._other_keys else 0 for key in union_keys]
    intersecton_keys = self._origin_keys & self._other_keys
    self._origin_values = [self.origin[key] for key in intersecton_keys]
    self._other_values = [other[key] for key in intersecton_keys]

    d = (norm(self._origin_values)*norm(self._other_values))
    if d == 0:
      return 0
    return dot(self._origin_values, self._other_values)/d

  

