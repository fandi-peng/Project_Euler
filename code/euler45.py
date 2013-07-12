

def tri(n):
    return n * (n + 1) / 2

def pent(n):
    return n * (3 * n - 1) / 2

def hexa(n):
    return n * (2 * n - 1)

def three():
    for i in range(286, 1000000):
        triangle = tri(i)
        for j in range(2, i):
            if triangle == pent(j):
                for k in range(2, j):
                    if triangle == hexa(k):
                        return triangle

print three()
    

