
with open('matrix.txt') as f:
    content = f.readlines()
    matrix = [[int(j) for j in i.split(',')]
               for i in ''.join(content).split('\n') if i] 


test_m = [[131,  673, 234, 103, 18], 
          [201,  96,  342, 965, 150], 
          [630,  803, 746, 422, 111], 
          [537,  699, 497, 121, 956],
          [805,  732, 524, 37,  331],
          ]

def make_matrix(m):
    m.insert(0, [999999999999]*len(m[0]))
    m.insert(len(m)+1, [99999999999999]*len(m[0]))
    new_m = [[] for x in range(len(m[0]))]
    for l in m:
        for pos, i in enumerate(l):
            new_m[pos].append(i)
    return new_m
            
def path_sum(m):
    for h in m:
        print h
    print 
    while len(m) > 1:
   # for k in range(2):
    #    print m; print
        nl = list(m[-2])
        for p, i in enumerate(m[-2]):
            if p > 0 and p < len(m[0]) - 1: 
                v2 = i + m[-1][p-1] + m[-2][p-1]
                v1 = i + m[-1][p]
                v3 = i + m[-1][p+1] + m[-2][p+1]
                nl[p] = min(v1, v2, v3)
        m[-2] = nl
        print m[-2]
        m.pop(-1)
    return min(m[0])
        
            
   # return m


fm = make_matrix(test_m)
print path_sum(fm)
print fm





