def collatz_sequence(candidate):
    all_length = []
    for i in range(candidate):
        print i
        length = 1
        while i > 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = 3 * i + 1
            length += 1
        all_length.append(length)

    m = max(all_length)
    return [i for i, j in enumerate(all_length) if j == m]


print collatz_sequence(1 * 10 ** 6)
