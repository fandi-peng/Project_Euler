import math

def amicable(n):
    gap = int(math.sqrt(n)) + 1
    a = set([])
    for i in range(1, gap):
        d, m = divmod(n, i)
        if m == 0:
           a = a | set([d, i]) 
    return sum(a - set([n]))

def chain(n):
    chain = []
    a = amicable(n)
    print n
    while True:
        chain.append(a)
        print chain
        if a == n:
            return chain
        next_a = amicable(a)
        if (a == next_a or next_a > 10 ** 6 or amicable(next_a) == a):
            return [] 
        a = next_a


#print list((chain(i) for i in range(1, 30) if chain(i)))
#print max((chain(i) for i in range(1, 10000 + 1)), key=len)
print chain(5916)


