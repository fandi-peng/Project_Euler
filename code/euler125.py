

def palin():
    return (i for i in range(2, 10**8) if str(i) == str(i)[::-1])

def cs(n):
#    print n
   # lower = i for 
    for x in range(1, int(n ** 0.5) + 1)[::-1]:
        s = x ** 2
        for y in range(1, x)[::-1]:
           # print x, y, s
            s += y ** 2
            if s > n:
                break
            if s == n:
                return n
    return 0



#print sum(cs(i) for i in palin())
s = 0
for p, i in enumerate(list(palin())[::-1]):
    print p
    s += cs(i)
print s
