def fibo():
    a = 1
    b = 1
    pos = 2
    while True:
        a = a + b
        b = a + b
        pos += 2
        if len(str(a)) >= 1000:
            return pos - 1, a
        if len(str(b)) >= 1000:
            return pos, b

print fibo()
