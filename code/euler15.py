def lattice(n):
    a = 0
    for i in range(1, n):
        a += 2 ** i
    return a * 2 + 2 ** n

print lattice(2)
print lattice(3)
print lattice(4)
print lattice(5)
print lattice(20)
