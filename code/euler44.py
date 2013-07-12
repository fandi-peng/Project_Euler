

cache = {}


def penta(n):
    return n * (3 * n - 1) / 2

for i in range(1, 1 * 10 ** 2): 
    cache[i] = penta(i)

l = cache.values()

def check_penta():
    n = 1
  #  while True:
    for k in range(1 * 10 ** 4):
       # print n
        for i in range(1, n)[::-1]:
            if cache[n] - cache[i] in l and cache[n] + cache[i] in l:
                return n, i, cache[n], cache[i], cache[n] - cache[i]
        n += 1

def get_diff():
    n = 1
    while True:
        if penta(n+1) - penta(n) >= 5482660:
            return n

        n += 1

print get_diff()
