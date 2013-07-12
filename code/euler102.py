from sympy import *
from sympy.geometry import *


with open('triangles_102.txt') as f:
    content = f.readlines()
    t = [[int(j) for j in i.strip().split(',')] for i in content if i]
    p = [Triangle(Point(a,b), Point(c,d), Point(e,f)) for 
         a, b, c, d, e, f in t]

O = Point(0, 0)

c = 0
for i in p:
    if i.encloses_point(O):
        c += 1
print c





