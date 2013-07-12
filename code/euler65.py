
from fractions import Fraction as F

def convergent(n):
    # while True:
    for i in range(5):
        if n % 3 == 2:
            n = 1 / (1 + ((n + 1) / 3 * 2 ))
        elif n % 3 == 1:
            n = 1 / (1 + 1)
        elif n % 3 == 0:
            n = 

            n -= 1
