from neighborhood import Neighborhood

def test_one_to_one():
    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    b = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 5}
    n = Neighborhood(a, 0.7, 5)
    n.setNeighbors([b])
    print(n.getNeighbors())
    print(n.recomend(3))



if __name__ == '__main__':
    test_one_to_one()