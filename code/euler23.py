import math

def find_divisors(n):
    cut = int(math.sqrt(n))
    divisors = []
    for i in range(1, cut+1):
        if n % i == 0:
            divisors.append(i)
            if n / i not in divisors:
                divisors.append(n / i)
    if len(divisors) > 1:
        divisors.pop(1)
    return divisors

def is_abundant(n):
    divisors = find_divisors(n)
    return sum(divisors) > n
    
def is_abundant_sum(candidate_sum):
    for i in range(candidate_sum + 1):
        if is_abundant(i) and is_abundant(candidate_sum - i):
            return True
    return False

def non_abundant_sum():
    upper_limit = 28123 + 1
    total = 0
    for i in range(1, upper_limit):
        if not is_abundant_sum(i):
            print i
            total += i
    return total

print non_abundant_sum()

