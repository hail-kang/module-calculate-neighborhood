import abc
from .neighborhood import Neighborhood

class Recommend(metaclass=abc.ABCMeta):
  
  @abc.abstractclassmethod
  def add(self):
    pass

  @abc.abstractclassmethod
  def report(self):
    pass