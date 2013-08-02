import pandas as pd


with open('matrix.txt') as f:
    content = f.readlines()
    matrix = [[int(j) for j in i.split(',')]
               for i in ''.join(content).split('\n') if i] 

matrix = [[131, 673, 234, 103, 18],
[201, 96, 342, 965, 150],
[630, 803, 746, 422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524, 37,  331]]
    

df = [i[1:] for i in pd.DataFrame(matrix).T.itertuples()]



def min_path(l1, l2):
    new_l = []
    for pos, i in enumerate(l1):
        way1 = l1[pos] + l2[pos] 
        try:
            way2 = l1[pos] + l1[pos+1] + l2[pos+1]
        except IndexError:
            way2 = 9999999
        try:
            way3 = l1[pos] + l1[pos-1] + l2[pos-1]
        except IndexError:
            way3 = 9999999
        if pos == 0:
            way3 = 9999999
     #   print way1, way2, way3
        new_l.append(min(way1, way2, way3))
  #  print new_l
    return new_l


def get_path(m):
    while len(m) >= 2:
        l2 = m.pop()
        m[-1] = min_path(m[-1], l2)
    print m
    return min(m[-1])


#print min_path(df[0], df[1])

print get_path(df)





