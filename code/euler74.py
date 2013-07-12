import math

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
def FofD(n):
    return sum(math.factorial(int(i)) for i in str(n))

def chain(n):
    l = []
    while True:
        l.append(n)
        n = FofD(n)
        if n in l:
            return len(l)

print map(chain, range(10**6)).count(60)
