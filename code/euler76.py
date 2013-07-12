

def cs(n):
    c = n - 1
    d = {i:n-i for i in range(1, n)}
    for i in xrange(2, n):
        for j in d:
            if i <= j:
                c += d[j] / i 
    return c



print cs(100)
