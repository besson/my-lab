def sort(a):
    if (len(a) == 1):
        return a
    else:
        a1 = sort(a[0:len(a)/2])
        a2 = sort(a[len(a)/2:len(a)])

        return merge(a1, a2)


def merge(a, b):
    size = len(a) + len(b)
    result = []
    i = 0
    j = 0

    for k in range(0, size):
        if (i < len(a) and j < len(b)):

            if (a[i] <= b[j]):
                result.append(a[i])
                i = i + 1
            else:
                result.append(b[j])
                j = j + 1

        else:
            if (i < len(a)):
                result.append(a[i])
                i = i + 1
            else:
                result.append(b[j])
                j = j + 1

    return result