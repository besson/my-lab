# function that receives and array and removes the duplicates, I want to investigate how to do it with
# better space complexity

def remove_duplicates(a):
	counts = {}
	result = []


	for i in range(len(a)):
		if (a[i] not in counts):
			counts[a[i]] = 1
			result.append(a[i])


	return result

