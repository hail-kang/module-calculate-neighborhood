from numpy import dot
from numpy.lib.function_base import iterable
from numpy.linalg import norm

class Cosine:
    def __init__(self, info:dict, proximity:float):
        self.info:dict = info
        self.elements:set = set(info.keys())

        #neighbor로 추가할 최소 근접도
        self.proximity:float = proximity

        #neighborKeys - mykeys (추천할 elements)
        self.candidate_element:set = set()

    def cos_similarity(self, A:list, B:list) -> float:
        D:float = (norm(A)*norm(B))
        if D == 0:
            return 0
        return dot(A, B)/D
    
    def fit(self, neighborhood:dict) -> None:
        self.candidate_element |= set(neighborhood.keys())
        self.candidate_element -= self.elements

    def predict(self, neighborhoods:iterable, infimum:float) -> list:
        recommend_list:list = []
        element:object
        for element in self.candidate_element:
            M:float = 0
            R:float = 0

            neighborhood: dict
            for neighborhood in neighborhoods:
                neighborhood_elements:set = set(neighborhood.keys())
                intersection:set = self.elements & neighborhood_elements

                my_vector:list = [self.info[e] for e in intersection]
                neigborhood_vector:list = [neighborhood[e] for e in intersection]

                p:float = self.cos_similarity(my_vector, neigborhood_vector)
                v:float = neighborhood.get(element)

                if v != None and v >= self.proximity:
                    M += p
                    R += 1
            
            if R > 0 and M/R >= infimum:
                recommend_list.append({ 'element' : element, 'probability' : M/R })

        return recommend_list

cos = Cosine({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 0.7)
cos.fit({'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 5})
r = cos.predict([{'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 5}], 0.7)
print(r)