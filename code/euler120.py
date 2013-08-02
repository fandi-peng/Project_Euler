
def sr(a):
    p = []
    n = 1
    while True:
        p.append(((a - 1) ** n + (a + 1) ** n) % a ** 2)
        l = len(p)
        if l > 6:
            if p[:l/3] == p[l/3:l/3*2] == p[l/3*2:]:
                return max(p)
        n += 1

print sum(sr(i) for i in range(3, 1001))
