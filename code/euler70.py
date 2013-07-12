import pyprimes

def permu(x, y):
    return sorted(str(int(x))) == sorted(str(int(y)))

def tot(x, y):
    return (x - 1) * (y - 1)

r = set(pyprimes.primes_below(5000)) - set(pyprimes.primes_below(2000))
l = ((i, j)  for i in r for j in r 
     if i * j < 10 ** 7 and permu(tot(i, j), i * j))
x, y =  min(l, key=lambda i: i[0] * i[1] / float(tot(i[0], i[1])))
print x * y  
