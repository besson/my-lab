# move in-place zeros to left and count the number of non-zeros

def move_and_count(a):
	j = len(a) - 1
	i = non_zeros = 0

	while (i <= j):
		if (a[i] == 0):
			while (a[j] == 0):
				j = j - 1

			if (j > i):
				non_zeros = non_zeros + 1
				a[i] = a[j]
				a[j] = 0
				j = j - 1
		else:
			non_zeros = non_zeros + 1

		i = i + 1

	return non_zeros