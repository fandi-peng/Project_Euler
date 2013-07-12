def combinations(n, coins):
   m = [1] * (n + 1)
   for c in coins[1::]:
      for i in xrange(c, n + 1):
         print i - c
         m[i] += m[i - c]
   print m
   return m[n]

print combinations(10, [1, 2, 5, 10, 20, 50, 100, 200])
















coins = [200, 100, 50, 20, 10, 5, 2, 1]

def get_combo(combos):
    pos_1 = [pos for pos, x in enumerate(combos[-1]) if x ==1]
    if pos_1:
        if pos_1[0] == 0:
            return combos
        pos = pos_1[0] - 1
    else:
        pos = -1
    new_combo = combos[-1][:pos]
    last_coin = combos[-1][pos]
    next_pos = [p for p, i in enumerate(coins) if i == last_coin][0] + 1
    while True:
        if (sum(new_combo) + coins[next_pos]) <= 200:
            new_combo.append(coins[next_pos])
        else:
            next_pos += 1
            if next_pos >= len(coins):
                break
    combos.append(new_combo)
    return combos

def all_combos():
    combos = [[200]]
    while combos[-1][0] != 1:
        combos = get_combo(combos)
    return len(combos)

# print all_combos()






    

