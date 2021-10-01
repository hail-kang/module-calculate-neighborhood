from neighborhood import Cosine
import unittest

class NeigborhoodTest(unittest.TestCase):
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
        
        cos = Cosine(users[0], 0.7)
        for nei in users[1:]:
          cos.fit(nei)

        # print('=====nei===')
        # for nei in n.getNeighbors():
        #     print(nei)

        # with open('users.txt', 'wt') as f:
        #     for user in n.getNeighbors():
        #         f.write(f'{user}\n')

        print('=====anly===')
        # for rec in n.recomend(1):
        #     print(rec)
        for rec in cos.predict(users[1:], 0.6):
          print(rec)
        print('============')

if __name__ == '__main__':
  unittest.main()