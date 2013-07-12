import itertools

def transform(lst):
    return ''.join(str(elem) for elem in lst)

def all_combo():
    s = list(itertools.permutations('0123456789'))
    l = [i for i in s if i[0] != '0' and i[5] in ('0', '5')]
    return l

def check_pattern(n):
    checker = [1, 2, 3, 5, 7, 11, 13, 17]
    for pos in range(1, len(n)-2):
        if int(n[pos: pos+3]) % checker[pos] != 0:
            return False
    return True
    
def check():
    l = []
    for p, i in enumerate(all_combo()):
        t = transform(i)
        if check_pattern(t):
            l.append(int(t))
    return sum(l)


print check()
