
cache = []

def rev(n):
    n = str(n)
    if n not in cache and n[-1] != '0':
        d = [int(i) for i in str(int(n) + int(n[::-1]))]
        if all(i % 2 != 0 for i in d):
            print n
            cache.append(n)
            cache.append(n[::-1])




for i in xrange(10 ** 9 + 1):
    rev(i)


print len(cache)


