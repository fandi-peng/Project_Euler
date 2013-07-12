import pyprimes

def distinct_factors(n):
    return len(set(pyprimes.factors(n)))

def four_consec():
    i = 2
    while True:
        i += 1
        if distinct_factors(i) != 4:
            continue
        if distinct_factors(i+1) != 4:
            continue
        if distinct_factors(i+2) != 4:
            continue
        if distinct_factors(i+3) != 4:
            continue
        return i
        

print four_consec()
