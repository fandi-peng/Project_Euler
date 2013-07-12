from fractions import Fraction

def canc_frac(b, a):
    all_digits = ' '.join(str(b)+str(a)).split()
    if '0' in all_digits:
        return None
    l = [i for i in all_digits if all_digits.count(i) == 1]
    if len(l) == 2:
        return float(l[0]) / float(l[1])
    
    

def luck_frac():
    for a in range(10, 100):
        for b in range(10, a):
            if canc_frac(b, a) == float(b) / float(a):
                print b, a, float(b) / float(a)


print luck_frac()

#rint canc_frac(10, 20)
