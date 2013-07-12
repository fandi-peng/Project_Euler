from itertools import permutations
import pyprimes
import numpy

def primes_candidates():
    return [i for i in list(pyprimes.primes_below(10000)) if i > 1000]

def prime_permute(p):
    l = list(permutations(str(p)))
    a = [int(''.join(i)) for i in l if i[0] != '0']
    primes = sorted(set([x for x in a if pyprimes.isprime(x)]))
    return primes


def find_arithmetic_sequence(i, l):
    diff = [j - i for j in l]
    for d in diff:
        if 2 * d in diff:
            return i, i + d, i + 2 * d

def arithmetic_primes(l):
    for pos, i in enumerate(l):
        a = find_arithmetic_sequence(i, l[pos+1:])
        if a:
            return a

def run():
    for i in primes_candidates():
        p = arithmetic_primes(prime_permute(i))
        if p:
            print p


print run()
