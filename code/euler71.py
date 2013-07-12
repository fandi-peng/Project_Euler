from fractions import Fraction as F

a, g = 0, F(3, 7)
for i in range(1, 10 ** 6 + 1):
    f = F(int(g * i), i)
    if f > a and f < g:
        a = f


print a
