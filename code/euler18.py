
a = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

b = '''
3
7 4
2 4 6
8 5 9 3
'''
def get_triangle():
    s = ''
    f = open('triangle.txt')
    for line in f:
        s += line
    return s

def format_path(a):
    levels = []
    for i in a.strip().split('\n'):
        levels.append([int(j) for j in i.split()])       
    return levels

def every_path(n):  # find all routes for next n steps
    total_path = 2 ** (n)
    all_routes = []
    for i in range(total_path):
        route = "{0:b}".format(i)[::-1]  # use binary form to show each path
        if len(route) < n:
            route += '0' * (n - len(route))
        all_routes.append(route)
    return all_routes

# calculate max path value within n moves
def best_move(levels, level_pos, move_pos, n):  
    all_values = []
    all_paths = every_path(n)
    for path in all_paths:
        path_value = 0
        new_pos = move_pos
        for pos, move in enumerate(path):
            new_pos += int(move)
            path_value += levels[level_pos+1+pos][new_pos]
        all_values.append(path_value)
    max_pos = [i for i, j in enumerate(all_values) if j == max(all_values)][0]
    best_move = int(all_paths[max_pos][0])
    return best_move
        
def best_path(raw_path, n):
    levels = format_path(raw_path)
    path_value = 0
    move_pos = 0
    for level_pos, l in enumerate(levels):
        print level_pos
        path_value += l[move_pos]
        if n >= len(levels) - level_pos:
            n = len(levels) - level_pos - 1
        if level_pos == len(levels) - 1:
            return path_value 
        next_move = best_move(levels, level_pos, move_pos, n)
        move_pos += next_move
        

triangle = get_triangle()
print best_path(triangle, 13)
        
    

