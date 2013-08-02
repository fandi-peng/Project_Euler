
from math import factorial as f
from itertools import combinations


#def combo(n, k):
#    return f(n) / (f(k) * f(n-k))

def combo(n, k):
    return len(list(i for i in combinations(range(1, n+1), k) if 
            i[-1] - i[0] + 1 == k))

def all_combo(n):
    return sum(combo(n, k) for k in range(1, n+1))

n = 1
while True:
    a = all_combo(n)
    print a
    if a > 2 * 10 ** 6:
        print a
        break
    n += 1
