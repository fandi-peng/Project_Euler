from itertools import combinations
import pyprimes

p = pyprimes.primes_below(10 ** 8 / 2)

l = len(list(i for i in combinations(p, 2) if i[0] * i[1] < 10 ** 8))

print l
