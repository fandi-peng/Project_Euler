import sys
sys.setrecursionlimit(10 ** 5)

def memo(f): # to cache 
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args) 
            return result
    return _f

def penta(n):
    k, p = 1, 0
    while p <= n:
        p, s = k * (3 * k - 1) / 2, (-1) ** (k - 1)
        yield p, s
        k *= -1
        p, s = k * (3 * k - 1) / 2, (-1) ** (k - 1)
        yield p, s
        k = k * -1 + 1

@memo
def p(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum(s * p(n - pt) for pt, s in penta(n))

def run():
    n = 1
    while True:
        if p(n) % 10 ** 6 == 0:
            return n
        n += 1

#print run()
print p(4096)




