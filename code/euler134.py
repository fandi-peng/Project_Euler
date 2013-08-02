
import pyprimes

p = list(pyprimes.primes_below(10 ** 6))

def pair_prime(p1, p2):
    print p1, p2
    n = 3
    while True:
        if str(p2 * n)[-len(str(p1)):] == str(p1):
           # print n
            return p2 * n
        n += 2

print sum(pair_prime(p[pos-1], i) for pos, i in enumerate(p) if pos >= 3)

