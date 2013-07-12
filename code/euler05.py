def find_multiple():
    a = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    while True:
        is_multiple = True
        for i in range(11, 21):
            if a % i != 0:
                is_multiple = False
                break
        if is_multiple:
            return a
        else:
            a += 1

print find_multiple()
            
            
