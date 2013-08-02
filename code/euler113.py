
def bouncy(n):
    l, s = list(str(n)), sorted(str(n))
    return l != s and l != s[::-1]

def find_percent():
    n, d = 0, 1
    while True:
        if n / float(d) >= 0.99:
            return d
        n, d = n + bouncy(d+1), d + 1



def nonbouncy():
    s = 0
    for a in range(1, 10):
        for b in range(1, a+1):
            for c in range(1, b+1):
                s += 1
                print c, b, a
    return s * 2 - 3


print sum(bouncy(i) for i in range(1000))
print nonbouncy()
