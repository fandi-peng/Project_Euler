
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
def w(t, c, coin):
    if c == 1 or t == 0:
        return 1
    else:
        i = t / c
        return sum(w(t - i*c, coin[coin.index(c)+1], coin) for i in range(i+1))

def cp():
    n = 10
    while True:
        coin = tuple(range(1, n+1)[::-1])
        s = w(n, n, coin)
        coin2 = tuple(range(1, n)[::-1])
        s2 = w(n-1, n-1, coin2)
        if s % 10 ** 6 == 0:
            return n
        print n, s, s - s2
        n += 1


print cp()
    
    
    

