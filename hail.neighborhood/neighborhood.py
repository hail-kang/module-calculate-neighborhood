import abc

class Neighborhood(metaclass=abc.ABCMeta):

  @abc.abstractclassmethod
  def add(self):
    pass

  @abc.abstractclassmethod
  def report(self):
    pass
