import itertools

def permute(s):
    l = ' '.join(s).split()
    return list(itertools.permutations(l))


print permute('0123456789')[10 ** 6 - 1]
