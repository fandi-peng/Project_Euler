total = 2
a = 1
b = 2
while True:
    a = a + b
    if a % 2 == 0:
        total = total + a
    b = a + b
    if b % 2 == 0:
        total = total + b
    if a >= 4 * 10 ** 6 or b >= 4 * 10 ** 6:
        break


print total
