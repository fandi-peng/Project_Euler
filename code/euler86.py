from fractions import gcd
from collections import Counter

def multi(t):
    a, b, c = t
    m = 1
    while max((a * m, b * m)) <= 99 * 2:
        yield a * m,  b * m,  c * m
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

def s(t):
    a, b, c = t
    p = []
    for i in range(1, a/2+1):
        if b <= 99 and i <= 99 and a-i <= 99:
            p.append((b, i, a - i))
    for j in range(1, b/2+1):
        if a <= 99 and j <= 99 and b-j <= 99:
            p.append((a, j, b - j))
    return p

def all_t():
    a = []
    for i in right_angle():
        a += s(i)
    k = list((j[0] * j[1] * j[2] for j in a))
    return set(k)

#print len(right_angle())
#print Counter(right_agle()).values().count(1)
#print s((6, 8, 10))
print len(all_t())
            
   
