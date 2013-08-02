

code = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def get_l():
    with open('roman.txt') as f:
        content = f.readlines()
    l = []
    t_before = 0
    for n in content:
        n = n.strip()
        t_before += len(n)
        l.append(sum(code[c] for c in n))
    return l, t_before

def min_exp(x):
    n = sorted(code.values())
    c = 0
    while len(n) > 1:
        if x - n[-1] > 0:
            x -= n[-1]
            c += 1
        else:
            n.pop()
    print x
    return c + x 

def all_saved():
    l, t_before = get_l()
    t_after = sum(min_exp(n) for n in l)
    return t_after - t_before


print all_saved() 

