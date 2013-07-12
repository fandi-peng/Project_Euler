from collections import Counter

with open('cipher1.txt') as f:
    content = eval('[' + f.readlines()[0][:-1] + ']')

def group_keys():
    groups = [[],[],[]]
    for pos, i in enumerate(content):
        groups[pos % 3].append(i)
    
    first = Counter(groups[0])
    second = Counter(groups[1])
    third = Counter(groups[2])
    print first, '\n'
    print second, '\n'
    print third, '\n'

def translate():
    t = []
    pw = (103, 111, 100)
    for pos, i in enumerate(content):
        t.append(chr(i ^ pw[pos % 3]))
    return ''.join(t)

print group_keys()
print translate()
