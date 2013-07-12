from pyprimes import isprime

def truncate(n):
    l = []
    for i in range(len(str(n))):
        l.append(int(str(n)[:i+1]))
        l.append(int(str(n)[::-1][:i+1][::-1]))
    return l[:-1]

def prime_check(l):
    for i in l:
        if not isprime(i):
            return False
    return True

def all_truncatable():
    i = 8
    l = []
    while len(l) < 11:
        if isprime(i):
            if prime_check(truncate(i)):
                l.append(i)
                print i
        i += 1
    return sum(l)


print all_truncatable()
