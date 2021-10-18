import abc

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


