for c in range(1000/3, 500):
    for a in range(1000 - c):
        b = 1000 - a - c
        if c ** 2 == a ** 2 + b ** 2:
            print a, b, c, a * b * c
            break
