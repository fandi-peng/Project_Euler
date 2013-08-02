from itertools import permutations

def xx():
    X = (j for j in permutations(range(0, 10), 3) if sum(j) <=9)
                



print xx()
