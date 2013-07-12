def right_tri(i):
    l = []
    for c in range(i/3, i/2):
        for a in range(1, (i - c)/2 + 1):
            b = i - c - a
            if b >= c:
                continue
            o = sorted([a, b, c])
            if o[0] ** 2 + o[1] ** 2 == o[2] ** 2:
                l.append(o)
    if l:
        return len(l), i


def all_combo():
    most = [0, 0]
    for i in range(10, 1001):
        q = right_tri(i)
        if q and q[0] > most[0]:
            most = q
    return most
        


print all_combo()

