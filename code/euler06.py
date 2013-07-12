sum_of_squares = 0
sums = 0
for i in range(1, 101):
    sum_of_squares += i ** 2
    sums += i

print abs(sum_of_squares - sums ** 2)
