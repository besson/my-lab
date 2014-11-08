#Given two strings, return boolean True/False, if they are only one edit apart.
#Edit can be insert/delete/update of only one character in the string. 

def are_closer(str1, str2):
	diff = abs(len(str1) - len(str2)) 

	if (diff > 1):
		return False
	else:
		bigger = small = ""

		if (len(str1) > len(str2)):
			bigger = str1
			small = str2
		else:
			bigger = str2
			small = str1

		changes = j = 0

		for i in range(len(bigger)):
			if (changes == 0) and (i == len(small)):
				changes = changes + 1
			elif (bigger[i] == small[j]):
				j = j + 1
			else:
				changes = changes + 1
				if (diff == 0):
					j = j + 1 

	return changes == 1