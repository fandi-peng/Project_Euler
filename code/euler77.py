import pyprimes

def memo(f): # to cache 
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args) 
            return result
    return _f

@memo
def w(t, c, l):
    if t == 0 or c == t == 2:
        return 1
    elif c == 2 != t:
        if t % c == 0:
            return 1
        return 0
    else:
        i = t / c
        return sum(w(t - j * c, l[l.index(c)-1], l) for j in range(i+1))

def pw():
    i = 2
    while True:
        l = tuple(pyprimes.primes_below(i))
        c = l[-1]
        if w(i, c, l) > 5000:
            return i
        i += 1


print pw()
