from itertools import product, combinations
import pyprimes

primes = list(pyprimes.primes_below(10000))

def pair_prime():
    for a in primes:
        for b in primes:
            if b > a and a != b and prime_check([a, b]):
                for c in primes:
                    if (c > b and len(set([a, b, c])) == 3 and 
                        prime_check([a, b, c])):
                        for d in primes:
                            if  (d > c and 
                                 len(set([a, b, c, d])) == 4 and 
                                 prime_check([a, b, c, d])):
                                for e in primes:
                                    if (e > d and 
                                        len(set([a, b, c, d, e])) and 
                                        prime_check([a, b, c, d, e])):
                                        return  a+b+c+d+e

def prime_check(p):
    l = [str(x) + str(y) for x, y in product(p, p) if x != y]
    return all(pyprimes.isprime(int(i)) for i in l)


print pair_prime()

