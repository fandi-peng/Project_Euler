import numpy as np

def get_hands():
    with open('poker.txt') as f:
        hands = f.readlines()
    return [i.split() for i in hands]

def read_cards(l):
    cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    hand = []
    for s in l:
        if s[0] in cards:
            hand.append((cards[s[0]], s[1]))
        else:
            hand.append((int(s[0]), s[1]))
    return hand

def flush(c):
    f = [i[1] for i in c]
    return len(set(f)) == 1

def straight(s):
    return np.diff(s)[0] == 1 and len(set(np.diff(s))) == 1
    
def same_kind(s):
    if len(set(s)) == 5:
        return False
    return set([(i, s.count(i)) for i in s if s.count(i) > 1])

def one_hand(h):
    hand = read_cards(h)
    s = sorted([i[0] for i in hand])
    level = {}
    if straight(s) and flush(hand):
        level['straight flush'] = s[-1]
    if flush(hand):
        level['flush'] = s[-1]
    if same_kind(s):
        same = list(same_kind(s))
        if len(same) == 1:
            if same[0][1] == 4:  # how many same kinds
                level['four of a kind'] = same[0][0]
            if same[0][1] == 3:
                level['three of a kind'] = same[0][0]
            if same[0][1] == 2:
                level['one pair'] = same[0][0]
            s = [i for i in s if i != same[0][0]]
        elif len(same) == 2:
            if same[0][1] == 3:
                level['full house'] = same[0][0]
                s = []
            elif same[1][1] == 3:
                level['full house'] = same[1][0]
                s = []
            else:
                level['two pairs'] = sorted((same[1][0], same[0][0]))[-1]
                s = [i for i in s if i != same[0][0] and i != same[1][0]]
    elif straight(s):
        level['straight'] = s[-1]
        s = []
    level['high'] = s[::-1]
    return level

def compete(l):
    p1, p2 = read_cards(l[:5]), read_cards(l[5:])
    h1, h2 = one_hand(p1), one_hand(p2)
    s = ['straight flush', 'four of a kind', 'full house', 
         'flush', 'straight', 'three of a kind', 'two pairs', 
         'one pair']
    winner = 0
    for i in s:
        if i in h1:
            if i not in h2:
                winner = 1
                break
            else:
                if h1[i] > h2[i]:
                    winner = 1
                    break
                elif h1[i] < h2[i]:
                    winner = 2
                    break
                if h1[i] == h2[i]:
                    continue
        else:
            if i in h2:
                winner = 2
                break
            else:
                continue
    if winner == 0:
        high1, high2 = h1['high'], h2['high']
        if high1:
            for pos, i in enumerate(high1):
                if pos < len(high2):
                    if i > high2[pos]:
                        winner = 1
                        break
                    elif i < high2[pos]:
                        winner = 2
                        break
    return winner


def play():
    c = 0
    for i in get_hands():
        if compete(i) == 1:
            c += 1
        elif compete(i) == 0:
            print 'holy shit', i
    return c


print play()


