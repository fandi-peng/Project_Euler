def f(n):
    m = 1
    for i in range(1, n+1):
        m *= i

    total = 0
    for l in str(m):
        total += int(l)
    return total


print f(100)
