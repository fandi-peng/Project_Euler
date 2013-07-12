
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

def sum_fact(s):
    return sum([sf[int(i)] for i in ' '.join(str(s)).split()])

sf = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 
      6:720, 7:5040, 8:40320, 9:362880}

def all_sum_fact():
    all_equal = []
    for i in range(10, 10000000):
        if i == sum_fact(i):
            print i
            all_equal.append(i)
    return all_equal, sum(all_equal)


#print sum_fact(20)

print all_sum_fact()
