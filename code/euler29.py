def distinct_powers(n):
    l = []
    for i in range(2, n+1):
        for j in range(2, n+1):
            l.append(j ** i)
    return len(set(l))


print distinct_powers(100)
