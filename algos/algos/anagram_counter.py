# Find all anagram in an array

class AnagramCounter:

	def __init__(self, a):
		self._array = a
		self._anagrams = {}

	def count(self):
		for word in self._array:
			s_word = self._sort_word(word)

			list = []
			if (s_word in self._anagrams.keys()):
				list = self._anagrams[s_word]

			list.append(word)
			self._anagrams[s_word] = list

		result = {}
		for key in self._anagrams.keys():
			for word in self._anagrams[key]:
				result[word] = len(self._anagrams[key])

		return result

	def _sort_word(self, word):
		# Assuming sort nlog(n)
		return ''.join(sorted(word))
