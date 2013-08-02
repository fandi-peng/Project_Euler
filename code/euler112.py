
def bouncy(n):
    l, s = list(str(n)), sorted(str(n))
    return l != s and l != s[::-1]

def find_percent():
    n, d = 0, 1
    while True:
        if n / float(d) >= 0.99:
            return d
        n, d = n + bouncy(d+1), d + 1

print find_percent()


