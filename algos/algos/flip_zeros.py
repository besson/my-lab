def get_flip_positions(array, m):
    i = j = wi = wj = zeros = 0
    window = -1
    flips = []

    while (i < len(array)):
        if (zeros <= m):
            if (array[i] == 0):
                zeros = zeros + 1
            i = i + 1

        if (zeros > m):
            if (array[j] == 0):
                zeros = zeros - 1
            j = j + 1

        if ((i - j) > window):
            window = (i - j)
            wi = i
            wj = j

    for k in range(wj, wi):
        if (array[k] == 0):
            flips.append(k)

    return flips