
def sd(n):
    while True:
        s = sum(int(i) ** 2 for i in' '.join(str(n)).split())
        if s == 89:
            return True
        elif s == 1:
            return False
        n = s

def run():
    c = 0
    for i in range(1, 10 ** 7 + 1):
        if sd(i):
            c += 1
    return c


print run()

#print sd(99)
