# Find all leaders elements
# An element is L-leader if all the elements following it are lesser than or equal to it. 

def find_leaders(array):
	solution = []
	solution.append(array[len(array) - 1])
	_max = array[len(array) - 1]

	for i in range(len(array) -2, -1, -1):
		if (array[i] >= _max):
			solution.insert(0, array[i])
			_max = array[i]

	return solution