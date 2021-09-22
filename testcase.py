from neighborhood import Neighborhood
import unittest

from numpy import dot
from numpy.linalg import norm
import numpy as np
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

class NeigborhoodTest(unittest.TestCase):
    def _test_percent(self):
        A = {'k': 3, 'y': 1, 'x': 4, 'v': 5, 'a': 2, 'i': 2, 'r': 5, 'u': 3, 'b': 0, 'e': 3, 'l': 3, 'n': 1, 'o': 1, 'z': 0, 'j': 5, 'w': 2, 'h': 5, 't': 2, 'g': 2, 's': 0, 'd': 0, 'c': 3, 'f': 3, 'p': 1, 'q': 5}
        B = {'k': 1, 't': 2, 'h': 5, 'w': 5, 'g': 1, 'v': 2, 'e': 4, 'p': 5, 'u': 4, 'b': 1, 's': 2, 'o': 5, 'f': 2, 'c': 3, 'l': 5, 'j': 3, 'z': 5, 'a': 4, 'r': 5, 'x': 3, 'd': 1, 'n': 2, 'y': 2, 'q': 2, 'i': 0, 'm': 0}
        A_keys = set(A.keys())
        B_keys = set(B.keys())
        ANB = A_keys.intersection(B_keys)
        AUB = A_keys.union(B_keys)

        # AUBL = list(AUB)
        # AUBL.sort()
        # for e in AUBL:
        #     print(f'{e}: {A.get(e)} {B.get(e)}')

        A_vals = [A[e] for e in ANB]
        B_vals = [B[e] for e in ANB]
        sim = cos_sim(A_vals, B_vals)
        print(sim)
            
        
        # E = 0
        # S = 0
        # for e in ANB:
        #     E += 5
        #     S += abs(A[e] - B[e])
        # if E == 0:
        #     print('0')
        # else:
        #     print((((len(ANB)+len(AUB))/(len(AUB)+len(AUB))) * (1 - S/E)))
            # print((((len(ANB)+len(AUB))/(len(AUB)+len(AUB))) * (1 - S/E)))

    def _test_one_to_one(self):
        print('======test_one_to_one======')
        # a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        # b = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 5}
        a = {'k': 3, 'y': 1, 'x': 4, 'v': 5, 'a': 2, 'i': 2, 'r': 5, 'u': 3, 'b': 0, 'e': 3, 'l': 3, 'n': 1, 'o': 1, 'z': 0, 'j': 5, 'w': 2, 'h': 5, 't': 2, 'g': 2, 's': 0, 'd': 0, 'c': 3, 'f': 3, 'p': 1, 'q': 5}
        b = {'k': 1, 't': 2, 'h': 5, 'w': 5, 'g': 1, 'v': 2, 'e': 4, 'p': 5, 'u': 4, 'b': 1, 's': 2, 'o': 5, 'f': 2, 'c': 3, 'l': 5, 'j': 3, 'z': 5, 'a': 4, 'r': 5, 'x': 3, 'd': 1, 'n': 2, 'y': 2, 'q': 2, 'i': 0, 'm': 0}
        
        
        n = Neighborhood(a, 0.7, 5)
        n.setNeighbors([b])
        print(n.getNeighbors())
        print(n.recomend(3))

    def test_random_many(self):
        print('=====test_random_many======')
        import random

        users = []
        for i in range(2000):
            user = dict()
            count = random.randint(1, 26)
            for j in random.sample(range(26), count):
                key = chr(ord('a') + j)
                value = random.randint(0, 5)
                user[key] = value
            users.append(user)

        # with open('users.txt', 'wt') as f:
        #     for user in users:
        #         f.write(f'{user}\n')

        print('=====init===')
        print(users[0])
        
        n = Neighborhood(users[0], 0.7, 5)
        n.setNeighbors(users[1:])

        print('=====nei===')
        for nei in n.getNeighbors():
            print(nei)

        print('=====anly===')
        for rec in n.recomend(1):
            print(rec)
        print('============')

if __name__ == '__main__':
    unittest.main()