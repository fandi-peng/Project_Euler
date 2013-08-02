from itertools import permutations
import pyprimes

def ppt():
    n = []
    for a in pyprimes.primes_below(7072):
        for b in pyprimes.primes_below(369):
            for c in pyprimes.primes_below(85):
                n += permu(a, b, c)
    return set(n)
    
def permu(a, b, c):
    return list(x ** 2  + y ** 3 + z ** 4 for 
                x, y, z in permutations((a, b, c)) if 
                x ** 2  + y ** 3 + z ** 4 < 50 * 10 ** 6)

print len(ppt())
