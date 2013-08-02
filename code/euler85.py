from math import sqrt

def all_divs(n):
    g = int(sqrt(n))
    l = []
    for i in range(1, g+1):
        if n % i == 0:
            l.append((i, n / i))
            l.append((n / i, i))
    return set(l)

def a_d(n):
    g = int(sqrt(n))
    l = []
    for i in range(1, g+1):
        if n % i == 0:
            l.append((i, n / i))
    return l

def count_rect(X, Y):
    s = 0
    for a in range(1, X * Y + 1):
        for x, y in all_divs(a):
            if X >= x and Y >= y:
                s += (X - x + 1) * (Y - y + 1)
    return s

def run():
    n = 1
    c = [99999999, 99999999]
    while True:
        for X, Y in a_d(n):
            cr = count_rect(X, Y)
            if abs(cr - 2 * 10 ** 6) < c[1]:
                c[0], c[1] = n, abs(cr - 2 * 10 ** 6)
                print c
        if n >= 5000:
            break
        n += 1 

run()
