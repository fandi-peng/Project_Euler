import pyprimes
from math import sqrt

def goldbach(n):
    p = list(pyprimes.primes_below(n))
    for i in p:
        a = sqrt((n - i) / 2.0)
        if a == int(a):
            return True
    return False

def non_conjecture():
    n = 1
    while True:
        n += 2
        if pyprimes.isprime(n):
            continue
        if not goldbach(n):
            return n
        
        
print non_conjecture()
