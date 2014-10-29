def print_diagonal(a):
    start = curr = 0

    for i in range(len(a)):
        if i + start < len(a):
            start = start + i
            curr = start

            for j in range(i, len(a)):
                if (j + curr < len(a)):
                    curr = curr + j
                    print "%d " % a[curr],

            print ""

print_diagonal([1, 2, 3,4,5,6,7,8])
print_diagonal([i for i in range(45)])