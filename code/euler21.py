import math


def divisors_sum(tri_num):
    cut = int(math.sqrt(tri_num))
    divisors = []
    for i in range(1, cut+1):
        if tri_num % i == 0:
            divisors.extend([i, tri_num / i])
    if len(divisors) >= 2:
        divisors.pop(1)  # delete the tri_num itself
    return sum(divisors)

def if_amicable(a):
    b = divisors_sum(a)
    if divisors_sum(b) == a and a != b:
        return True
    else:
        return False

def amicable_sum(n):
    amicables = []
    for i in range(n):
        if if_amicable(i) and i not in amicables:
            amicables.extend([i, divisors_sum(i)])
    return sum(amicables)



print amicable_sum(10000)
