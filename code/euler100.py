from sympy.abc import x, y
from sympy.solvers import solve
from fractions import Fraction as F
from math import sqrt

def ap():
    for i in range(10 ** 12 + 1, 10 ** 12 + 1000):
        solve(2 * x ** 2 - 2 * x - i ** 2 + i)


print ap()
