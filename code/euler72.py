import pyprimes
from operator import mul

def totient(n):
    p =  (1 - 1.0 / i for i in set(pyprimes.factors(n)))
    return n * reduce(mul, p, 1)

print sum(totient(i) for i in range(2, 10 ** 6 + 1))
