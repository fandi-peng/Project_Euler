def get_prime_candidate():
    prime_candidate = []
    for i in range(3, 2 * 10 ** 6):
        if str(i)[-1] not in ['0', '2', '4', '5', '6', '8']:
            prime_candidate.append(i)
    return prime_candidate



def prime_sum():
    prime_sum = 7
    prime_candidate_list = get_prime_candidate()

    for pos, prime_candidate in enumerate(prime_candidate_list):
        print pos
        is_prime = True
        for i in range(2, prime_candidate):
            if prime_candidate % i == 0:
                is_prime = False
                break
        if is_prime:
                prime_sum += prime_candidate

    return prime_sum


#print get_prime_candidate()
print prime_sum()

