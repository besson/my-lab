# Check if an expression has redundant braces

def has_redundant_braces(expression):
	ops = 0
	stack = []

	for w in expression:
		if w is "(":
			stack.insert(0, w)

		elif w is ")":
			if (ops == 0):
				return True
			else:
				stack.pop(0)
				ops = ops - 1

		elif not w.isalpha():
			ops = ops + 1


	return len(stack) > 0