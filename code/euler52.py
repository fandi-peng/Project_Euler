
def check(n):
    l = [n, n * 2, n * 3, n * 4, n * 5, n * 6]
    s = len(set([''.join(sorted(str(i))) for i in l]))
    return s == 1
        
n = 1
while True:
    if check(n):
        print n
        break
    n += 1




    
