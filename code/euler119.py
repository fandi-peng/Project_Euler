
def dps(n):
    return n  == sum(int(i) for i in str(n)) ** 3


#print dps(512)
for i in range(1, 10 ** 7):
    if dps(i):
        print i
