from itertools import permutations

def get_range():
    r = [[], [], [], [], [], []]
    for n in range(1, 200):
        l = [n * (n + 1) / 2, 
             n ** 2, 
             n * (3 * n - 1) / 2, 
             n * (2 * n - 1), 
             n * (5 * n - 3) / 2, 
             n * (3 * n - 2)]
        for pos, i in enumerate(l):
            if i >= 1000 and i < 10000:
                r[pos].append(i)
    return r

def cycl(l):
    tri, sq, pen, hexa, hep, octa = l
    return [(t, s, p, hx, hp, o)
            for t in tri
            for s in sq
            if str(t)[-2:] == str(s)[:2]
            for p in pen
            if str(s)[-2:] == str(p)[:2]
            for hx in hexa
            if str(p)[-2:] == str(hx)[:2]
            for hp in hep
            if str(hx)[-2:] == str(hp)[:2]
            for o in octa
            if str(hp)[-2:] == str(o)[:2]
            if str(o)[-2:] == str(t)[:2]
    ]

def run():
    ll = list(permutations(get_range()))
    for i in ll:
        if cycl(i):
            return cycl(i)


print run()
