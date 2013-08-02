
coin = range(1, 100)[::-1]


def memo(f): 
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
    return _f

@memo
def w(t, c):
    if c == 1 or t == 0:
        return 1
    else:
        i = t / c
        return sum(w(t - i*c, coin[coin.index(c)+1]) for i in range(i+1))

print w(100, 99)
    
    
    

