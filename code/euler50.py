
import pyprimes

all_primes = list(pyprimes.primes_below(1 * 10 ** 6))


def find_consec():
    l = 0
    for pos1, i in enumerate(all_primes):
        for pos2, j in enumerate(all_primes):
            if pos2 <= pos1:
                continue
            s = sum(all_primes[pos1:pos2]) 
            if s > 1 * 10 ** 6:
                print pos1
                break
            if s in all_primes and pos2 - pos1 > l:
                l = pos2 - pos1
                print s, l
                
        

find_consec()
