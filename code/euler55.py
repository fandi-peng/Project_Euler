
def lychrel(n):
    for i in range(50):
        candidate = n + int(str(n)[::-1])
        if str(candidate) == str(candidate)[::-1]:
            return False
        n = candidate
    return True

def check_all():
    c = 0
    for i in range(1, 10001):
        if lychrel(i):
            c += 1
    return c

print check_all()
