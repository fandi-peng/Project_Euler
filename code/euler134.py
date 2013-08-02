from fractions import gcd
import pyprimes

p = list(pyprimes.primes_below(10 ** 6))

def pair_prime(p1, p2):
    n, l = 3, 10 ** len(str(p1))
    while True:
        if p2 * n % l == p1:
            print p2, n
            return p2 * n
        n += 2

def pp(p1, p2):
    return gcd(p2, 10 ** len(str(p1))) * p2


#print sum(pair_prime(p[pos-1], i) for pos, i in enumerate(p) if pos >= 3)
print pp(19, 23)

#print pair_prime(19, 23)
