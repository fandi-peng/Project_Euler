
def pan_mul():
    pan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9000, 10000):
        p = i * 2
        l = [int(j) for j in (str(i) + str(p))]
        l.sort()
        if l == pan:
            print i, p

print pan_mul()
