from unittest import TestCase

class TestCipher:

	def test_decipher_4_rounds(self):
		message = decipher(7, 4, "1110100110")
		self.assertEquals("1001010", message)

	def test_decipher_2_rounds(self):
		message = decipher(6, 2, "1110001")
		self.assertEquals("101111", message)