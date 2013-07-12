number = 600851475143  # change it to the number you want to compute
prime = 2
while True:
    if number % prime == 0:
        print prime
        number = number / prime
    else:
        prime += 1
    if prime >= number:
        break
         

print prime

