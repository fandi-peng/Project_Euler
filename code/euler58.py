import pyprimes

def prime_count(n):
    c = range((n - 2) ** 2, n ** 2 + 1, n - 1)[1:]
    return len([i for i in c if pyprimes.isprime(i)])

def prime_ratio():
    total_primes = 0
    n = 3
    while True:
        total_primes += prime_count(n)
        ratio = float(total_primes) / (2 * n - 1)
        if ratio < 0.1:
            return n
        n += 2

print prime_ratio()
