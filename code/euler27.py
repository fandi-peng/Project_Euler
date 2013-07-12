def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def quadratic_primes(a, b):
    n = 0
    while True:
        p = n ** 2 + a * n + b
        if is_prime(p):
            n += 1
        else:
            break
    return n

def most_primes():
    largest = [0, 0]
    for a in range(-999, 1000):
        print a
        for b in range(2, 1000):
            if quadratic_primes(a, b) > largest[0]:
                largest[0], largest[1] = quadratic_primes(a, b), a * b
                print largest
    return largest
            
    
print most_primes()
