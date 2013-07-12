
def pds():
    s = (0, 0, 0)
    for q in range(1, 101):
        for m in range(1, 101):
            ll = ' '.join(str(q ** m)).split()
            l = sum([int(k) for k in ll])
            if l > s[2]:
                s = (q, m, l)
    return s
    
print pds()
