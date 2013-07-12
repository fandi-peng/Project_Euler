def pandigital():
    g = 0
    for a in range(1, 100):
        for b in range(100, 10000):
            c = a * b
            l = ' '.join(str(a) + str(b) + str(c)).split()
            l.sort()
            if l == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                g += c
    return g
            

print pandigital()
