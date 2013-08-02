import pyprimes

def memo(f): 
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
    return _f

#@memo
def w(t, c, l):
    if c == 2 or t == 0:
        return 1
    else:
        i = t / c
        return sum(w(t - i*c, l[l.index(c)+1], l) for i in range(i+1))



def prime_way():
    l = list(pyprimes.primes_below(10))[::-1]
    print l
    return w(10, 7, l)


print prime_way()
    
    
    

