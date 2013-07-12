def powers_sum(n):
    total = sum([int(i) ** 5 for i in str(n)])
    return total
   

def find_all():
    l = []
    for i in range(10, 400000):
        if i == powers_sum(i):
            l.append(i)
    return l, sum(l)


print find_all()

