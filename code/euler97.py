

def nmp():
    i = 28433
    c = 1
    while c <= 7830457:
        i = int(str(i * 2)[-10:])
        c += 1
    return i + 1


print nmp()
