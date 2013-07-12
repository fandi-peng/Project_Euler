from sympy import sqrt 
import math

def cont_frac(n):
    n = sqrt(n)
    while True:
        n = 1 / (n - int(n))
        print n
        yield int(n)

def period(cf):
    p = []
    while True:
        p.append(next(cf))
     #   print p
        l = len(p)
        if (l % 2 == 0 and len(set(p)) > 1 and p[:l/2] == p[l/2:]):
            return l / 2
        if l > 10:
            return 1

def run():
    odd_count = 0
    for i in range(1, 10000):
        print i
        if sqrt(i) == int(sqrt(i)):
            continue
        if period(cont_frac(i)) % 2 != 0:
            odd_count += 1
    return 'result:', odd_count

#print period(cont_frac(257))
#print run()
a = cont_frac(257)
for i in range(50):
    print next(a)
