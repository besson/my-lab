def sum_bin(a, b):
	result = []
	carry = 0

	maxlen = max(len(a), len(b))
	a = a.zfill(maxlen)
	b = b.zfill(maxlen)


	for i in range(len(a) -1, -1, -1):
		
		if (carry + int(a[i]) == 2):
			a1 = 0
			carry = 1
		else:
			a1 = int(a[i]) + carry

		_sum = a1 + int(b[i])

		if (_sum == 2):
			carry = 1
			result.insert(0, '0')
		else:
			result.insert(0, str(_sum))

	if (carry == 1):
		result.insert(0, '1')


	return ''.join(result)
