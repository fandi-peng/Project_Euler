
with open('matrix.txt') as f:
    content = f.readlines()
    matrix = [[int(j) for j in i.split(',')]
               for i in ''.join(content).split('\n') if i] 


test_m = [[1, 2, 5], [4, 3, 6], [7, 8, 9]]

def make_index(row):
    r = [1] * row
    return [(sum(r[:i]), sum(r[i:])) for i in range(row+1)[::-1]]

def fill_matrix(matrix):
    row_sum = len(matrix) * 2 - 1
    new_matrix = [[99999]*i for i in range(1, row_sum + 1)[::-1]]
    for p1, row in enumerate(matrix):
        for p2, i in enumerate(row):
            new_matrix[p1][p2] = matrix[p1][p2]
    return new_matrix
        
def final_matrix(new_matrix):
    fm = []
    for i in range(len(new_matrix)):
        index = make_index(i)
        fm.append([new_matrix[x][y] for x, y in index])
    return fm

def path_sum(matrix):
    while len(matrix[-1]) > 1:
        matrix[-2] = [min(i + matrix[-1][pos], i + matrix[-1][pos+1])
                      for pos, i in enumerate(matrix[-2])]
        print matrix[-2]
        matrix.pop()
    return matrix


nm = fill_matrix(matrix)
fm = final_matrix(nm)
print fm
print '***************************************'
print path_sum(fm)





