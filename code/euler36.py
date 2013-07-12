
def palindrome(n):
    b = "{0:b}".format(n)
    if str(b) == str(b)[::-1] and str(n) == str(n)[::-1]:
        return True


def palin_sum():
    l = []
    for i in range(1 * 10 ** 6):
        if palindrome(i):
            l.append(i)
    return sum(l)


print palin_sum()
