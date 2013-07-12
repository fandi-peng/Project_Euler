from pyprimes import nth_prime


def psr(p, n):
    return ((p - 1) ** n + (p + 1) ** n) % p ** 2

for i in range(21000, 21100):
    p = nth_prime(i)
    r = psr(p, i)
    print i, r, len(str(r))

