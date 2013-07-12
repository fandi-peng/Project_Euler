
def champ_con():
    a = '0123456789'
    s = '123456789'
    i = 1
    while True:
        for c in a:
            s += str(i) + c
        if len(s) > 10 ** 6:
            break
        i += 1
    return int(s[1-1]), int(s[10-1]), int(s[100-1]), int(s[1000-1]), int(s[10000-1]), int(s[100000-1]), int(s[1000000-1])

print champ_con()
