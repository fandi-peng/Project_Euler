from itertools import permutations
#import math
from scipy import special

#cubics = {i ** 3:i for i in range(1000)}
#cubics = [i ** 3 for i in xrange(1000)]

def permus(n):
    return set([int(''.join(i)) for i in 
             permutations(str(n)) if i[0] != '0'])

def cubic_permus():
    n = 1
    while True:
        #c = [x for x in permus(n ** 3) if x in cubics]
        c = [x for x in permus(n ** 3) if special.cbrt(x) == int(special.cbrt(x))]
        if len(c) == 5:
            return c
        n += 1
        print n

def cp():
    cubics = [i ** 3 for i in xrange(2000, 2500)]
    for pos, n in enumerate(cubics):
        c = 0
        for i in next_permu(n):
            if special.cbrt(i) == int(special.cbrt(i)):
                c += 1
                print c
                if c >= 5:
                    return n
        



def next_permu(n):
    return (int(''.join(i)) for i in set(permutations(str(n))) if i[0] != '0') 


#print cubic_permus()
#print cubics
#print next(a)
print cp()
