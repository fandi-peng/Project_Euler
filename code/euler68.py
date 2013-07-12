from itertools import permutations

def five_gon():
    return ((str(j), str(d), str(c),    str(i), str(c), str(b),    
             str(h), str(b), str(a),    str(g), str(a), str(e),    
             str(f), str(e), str(d)) for 
            (a, b, c, d, e, f, g, h, i, j) in 
            permutations(range(1, 11)) if 
            j + d + c == i + c + b == h + b + a ==
            g + a + e == f + e + d and min(j, i, h, g, f) == j)

print max(''.join(i) for i in five_gon() if i.count('10') == 1)

