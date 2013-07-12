from decimal import *

def get_decimal(n, p):
    getcontext().prec = p
    return str(Decimal(1) / Decimal(n))[2:]


def find_recursion(s):
    all_recursions = []
    for pos, i in enumerate(s):
        if i in s[:pos]:
            all_pre_pos = [p for p, x in enumerate(s[:pos]) if x == i]
            for pre_pos in all_pre_pos:
                if s[pre_pos:pos] == s[pos:pos+(pos-pre_pos)]:
                    if pos - pre_pos > 5:
                        all_recursions.append(s[pre_pos:pos])
    if all_recursions:
        return all_recursions[0]

def largest_recursion():
    largest = [0, '']
    decimals = 20
    for i in range(1, 1001):
        while True:
            s = get_decimal(i, decimals)
            if len(s) < decimals:
                break
            r = find_recursion(s)
            if r:
                if len(r) > len(largest[1]):
                    largest[0], largest[1] = i, r
                break
            else:
                decimals += 200
    return largest[0]
             

print largest_recursion()
