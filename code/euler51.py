import pyprimes

def sub_check(s):
    l = [s.replace('*', str(i)) for i in xrange(10)]
    p = [i for i in l if i[0] != '0' and pyprimes.isprime(int(i))]
    return p, len(p)


def change_pos(s):
    l = []
    for i in s:
        if s.count(i) > 1:
            l.append(s.replace(i, '*'))
    return set(l)

def run():
    p = pyprimes.primes()
    while True:
        s = str(next(p))
        l = change_pos(s)
        if l:
            for i in l:
                if sub_check(i)[1] == 8:
                    return sub_check(i)
                    


print run() 
