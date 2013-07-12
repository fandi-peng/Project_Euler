from fractions import Fraction as F

U, L = F(1, 2), F(1, 3)

def get_frac(n):
    return (F(i, n) for i in range(int(n * L) + 1, int(round(n * U))))

l = list(p for i in range(2, 12001) for p in get_frac(i))
print len(l), len(set(l))


def run():
    pf = []
    for i in range(2, 12001):
        for f in get_frac(i):
            if f not in pf:
                print i, f
                pf.append(f)

    return len(pf)

