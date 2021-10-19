from .similarity import Similarity

class Neighborhood:

  def __init__(self, similarity, threshold):
    if not isinstance(similarity, Similarity):
      raise Exception('similarity must be Similarity')
    self.similarity = similarity
    self.threshold = threshold
    self.neighborhoods = []

  def add(self, other):
    report = self.similarity.report(other)
    if report['distance'] > self.threshold:
      self.neighborhoods.append(report)

  def report(self):
    return self.neighborhoods