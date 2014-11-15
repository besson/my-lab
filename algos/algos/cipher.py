def decipher(size, rounds, message):

	cipher_msg = [int(i) for i in message]
	origin_msg = []
	origin_msg.append(cipher_msg[0])
	j = 0
	    
	for i in range(1, size):
		_char = int(bool(cipher_msg[i]) + bool(origin_msg[j]) == 1)
		k = j - 1

		for z in range(rounds - 2):
			if (k >= 0):
				_char = int(bool(_char) + bool(origin_msg[k]) == 1)
				k = k -1

		origin_msg.append(_char)
		j = j + 1

	return ''.join([str(i) for i in origin_msg])