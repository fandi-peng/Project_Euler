def spiral_diagonals(n):
    corner = [1]
    largest = n * n
    seq = range(1, largest+1)[::-1]
    for i in range(3, n+1, 2)[::-1]:
        for j in range(4):
            pos = i * j
            corner.append(seq[pos:pos+i][0])
            seq.insert(pos+i, seq[pos+i-1])
        seq = seq[pos+i:]
    print corner
    return sum(corner)
            

print spiral_diagonals(1001)


