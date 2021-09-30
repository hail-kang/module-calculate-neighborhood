from numpy import dot
from numpy.linalg import norm

class Neighborhood:
    def __init__(self, myInfo, proximity):
        self._me = myInfo
        self._neighbor = [] #(근접도, values) 리스트
        self.proximity = proximity #neighbor로 추가할 최소 근접도
        self._S = set() #neighborKeys - mykeys (추천할 elements)

    def getMyInfo(self):
        return self._me

    def getNeighbors(self):
        return self._neighbor

    def cosSimilarity(self, A, B):
        D = (norm(A)*norm(B))
        if D == 0:
            return 0
        return dot(A, B)/D

    def _percent(self, A, B):
        A_keys = set(A.keys())
        B_keys = set(B.keys())
        ANB = A_keys.intersection(B_keys)

        A_vals = [A[e] for e in ANB]
        B_vals = [B[e] for e in ANB]

        return self.cosSimilarity(A_vals, B_vals)

    def setNeighbors(self, users):
        self._S = set()
        mykeys = set(self._me.keys())
        for u in users:
            p = self._percent(self._me, u)
            if p > self.proximity:
                self._neighbor.append((p, u))
                self._S = self._S.union(set(u.keys()))
        self._S = self._S.difference(set(mykeys))

    def recomend(self, infimum):
        rL = []
        for e in self._S:
            M = 0 
            R = 0 
            for n in self._neighbor:
                p = n[0]
                v = n[1].get(e)
                if v != None and v >= infimum:
                    M += p
                    R += 1
            if R > 0:
                rL.append({ 'element' : e, 'probability' : M/R })
        return rL