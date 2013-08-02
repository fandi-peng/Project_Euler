from pyprimes import factors



def div_len(n):
    p = factors(n)
    return p

print div_len(36)
print div_len(1)
print div_len(2)
print div_len(3)
print div_len(4)
print div_len(5)
print div_len(6)

