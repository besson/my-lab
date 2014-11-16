def is_valid(sentence):
	alphabet = []

	for l in sentence:
		if l.isalpha():
			alphabet.append(l)

		
	return len(set(alphabet)) is 26