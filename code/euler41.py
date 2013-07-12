import pyprimes
import itertools

def candidates():
    candidates = []
    a = range(1, 8)
    l = list(itertools.permutations(a))[::-1]
    for i in l:
        s = ''
        if i[-1] % 2 == 0 or i[-1] % 5 == 0:
            continue
        for j in i:
            s += str(j)
        candidates.append(s)
    return candidates

def pan_prime():
    for i in candidates():
        if pyprimes.isprime(int(i)):
            return i


print pan_prime()
