from math import factorial

def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

c = 0
for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 10 ** 6:
            c += 1


print c
