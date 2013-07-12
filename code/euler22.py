def get_name():
    with open('names.txt', 'r') as f:
        a = f.read().split(',')
        a.sort()
        return a

def get_score(name, pos):    
    char_list = ' '.join(name).split()
    char_score = []
    for i in char_list:
        char_score.append(ord(i) - 64)  # ord('A') == 65
    return sum(char_score) * (pos + 1)

def total_score():
    names = get_name()
    total = 0
    for pos, i in enumerate(names):
        total += get_score(eval(i), pos)
    return total


print total_score()
    
