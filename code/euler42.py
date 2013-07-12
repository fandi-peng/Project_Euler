from math import sqrt
from sympy.abc import x
from sympy.solvers import solve

with open("words42.txt") as f:
    content = eval('[' + f.readlines()[0] + ']')

def is_triword(w):
    v = 0
    for i in w:
        v += ord(i) - 64
    r = max(solve(0.5 * x ** 2 + 0.5 * x - v))
    return r - int(r) == 0
    
def cal_all():
    count = 0
    for pos, i in enumerate(content):
        if is_triword(i):
            count += 1
    return count




print cal_all()
