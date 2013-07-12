import math


def divisors_length(tri_num):
    cut = int(math.sqrt(tri_num))
    divisors = []
    for i in range(1, cut+1):
        if tri_num % i == 0:
            divisors.extend([i, tri_num / i])
    return len(divisors)


def find_divisors():
    n = 1
    while True:
        tri_num = (1 + n) * n / 2
        n += 1
        if divisors_length(tri_num) > 500:
            return tri_num



print find_divisors()
