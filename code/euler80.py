from decimal import *

getcontext().prec = 110

def cd(n):
    if int(n ** 0.5) != n ** 0.5:
        s = str(Decimal(n) ** Decimal(0.5)).replace('.', '')
        return sum([int(i) for i in ' '.join(s).split()][:100])

print sum(cd(i) for i in range(1, 101) if cd(i)) 
