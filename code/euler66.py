import math
from fractions import Fraction as F

def memo(f): # to cache recursive function
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f

@memo
def cont_frac(s, n):
    if n == 0:
        m, d, a = 0, 1, int(math.sqrt(s))
        return m, d, a
    else:
        m, d, a = cont_frac(s, n-1)
        m = d * a - m
        d = F(s - m ** 2, d)
        a = int((math.sqrt(s) + m) / d)
        return m, d, a

def pd(s, n):
    return cont_frac(s, n)[2]

@memo
def conve(s, n):
    if n == 1:
        A = pd(s, 1) * pd(s, 0) + 1
        B = pd(s, 1)
        return A, B
    elif n == 2:
        A = pd(s, 2) * (pd(s, 1) * pd(s, 0) + 1) + pd(s, 0)
        B = pd(s, 2) * pd(s, 1) + 1
        return A, B
    else:
        A = pd(s, n) * conve(s, n-1)[0] + conve(s, n-2)[0]
        B = pd(s, n) * conve(s, n-1)[1] + conve(s, n-2)[1]
        return A, B

def diophantine(d):
    n = 1
    while True:
        try:
            x, y = conve(d, n)
            if x ** 2 - d * y ** 2 == 1:
                return x
        except ZeroDivisionError:
            return 0 
        n += 1
    
print max(range(2, 1001), key=diophantine)

