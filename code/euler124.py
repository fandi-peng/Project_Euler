from pyprimes import factors

def rad(n):
    return reduce(lambda x, y: x * y, set(factors(n)))

print sorted(xrange(1, 100001), key=rad)[10000-1]

