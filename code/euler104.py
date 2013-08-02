from math import sqrt

def fibo():
    a, b = 1, 1
    while True:
        yield str(a)
        a, b = b, a + b 


def pf():
    f = fibo()
    n = 0
    s = set([str(i) for i in range(1, 10)])
    while True:
        n += 1
        nf = next(f)
        if set(nf[:9]) == s:
            print n
            if set(nf[-9:])== s:
                return n


print pf()

