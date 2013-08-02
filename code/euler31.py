
coin = [200, 100, 50, 20, 10, 5, 2, 1]

def w(t, c):
    if c == 1 or t == 0:
        return 1
    else:
        i = t / c
        return sum(w(t - i*c, coin[coin.index(c)+1]) for i in range(i+1))

print w(200, 200)
    
    
    

