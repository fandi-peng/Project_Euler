from fractions import Fraction as F

def expan(n):
    if n == 1:
       return F(2) 
    else:
        return  2 + 1 / expan(n - 1)

def sqrt_c(n):
    return str(1 + 1 / expan(n)).split('/')

def run():
    c = 0
    for i in range(1, 1001):
        print i
        n, d = sqrt_c(i)
        if len(n) > len(d):
            c += 1
    return c

#print run()

print sqrt_c(10)
