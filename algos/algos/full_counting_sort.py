# based on https://www.hackerrank.com/challenges/countingsort4

def get_strings_in_order(size, _file):
	array = _build_array(_file)

	total = 0
	_max = -1

	for i in range(len(array)):
		if (array[i][2] >= _max):
			_max = array[i][2]

	count = [0 for i in range(_max)]
	output = ["-" for i in range(len(array))]

	for i in range(len(array)):
		key = array[i][0]
		count[key] = count[key] + 1

	for i in range(len(count)):
		temp = count[i]
		count[i] = total
		total = total + temp

	for i in range(len(array)):
		key = array[i][0]
		pos = count[key]

		if (array[i][2] >= size/2):
			output[pos] = array[i][1]

		count[key] = count[key] + 1

	return ' '.join(output)


def _build_array(_file):
	array = []
	i = 0

	for line in open(_file):
		entry = line.split()
		array.append([int(entry[0]), entry[1], i])
		i = i + 1

	return array
