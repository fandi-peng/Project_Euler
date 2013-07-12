
def n_rotation(n):
    s = str(n) + str(n)[:-1]
    l = len(str(n))
    r = []
    for i in range(l):
        r.append(int(s[i:i+l]))
    return r

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_candidate():
    candidates = [2, 5]
    valid_digit = '1379'
    for i in range(2, 1000000):
        valid = True
        for j in str(i):
            if j not in valid_digit:
                valid = False
                break
        if valid:
            if is_prime(i):
                candidates.append(i)
    return candidates

def circular_primes():
    cp = []
    candidates = find_candidate()
    print "*****************************"
    for i in candidates:
        l = n_rotation(i)
        all_prime = True
        for j in l:
            if not is_prime(j):
                all_prime = False
                break
        if all_prime:
            print i
            cp.append(i)
    return cp


print len(circular_primes())
