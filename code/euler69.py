
from pyprimes import factors

def relative_primes(n):
    f = factors(n)
    r = []
    for i in range(1, n):
        for j in f:
            if j in factors(i):
                print j, factors(i), i
                continue
            else:
                r.append(i)
    return set(r)



print relative_primes(10)
                
