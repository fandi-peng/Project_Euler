from itertools import permutations
import pyprimes


#c = (int(''.join(i)) for j in range(1, 10) for i in permutations('123456789', j))
#p = list(i for i in c if pyprimes.isprime(i))
#p = sorted(p)[::-1]

p = ['2', '5','7', '25', '47', '89', '631', '654321']#[::-1]

def prime_combo(c, t, l):
    if c == t:
        return 1
    elif c == 2:
        return 0
    else:
        candidates = [i + c for i in l if not set(i).intersection(set(c))]
         



                
        
        
    

c = p.pop
print prime_combo(c, '123456789', p)
    
