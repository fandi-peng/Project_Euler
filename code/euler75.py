from fractions import gcd
from collections import Counter

def multi(t):
    a, b, c = t
    m = 1
    while a * m + b * m + c * m <= 1500000:
        yield a * m + b * m + c * m
        m += 1

def right_angle():
    l = []
    for n in range(1, 900):
        for m in range(n, 900):
            if gcd(m, n) == 1 and (m - n) % 2 != 0:
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                l += list(multi((a, b, c)))
    return l

print Counter(right_angle()).values().count(1)


            
   
