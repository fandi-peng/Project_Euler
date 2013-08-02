
def palin():
    return (i for i in range(2, 10**8) if str(i) == str(i)[::-1])

def cs(n):
    for x in range(1, int((n / 2) ** 0.5) + 2)[::-1]:
        if x * (x + 1) * (2 * x + 1) / 6.0 < n:
            break
        s = x ** 2
        for y in range(1, x)[::-1]:
            s += y ** 2
            if s > n:
                break
            if s == n:
                print n
                return n
    return 0

print sum(cs(i) for i in palin())


