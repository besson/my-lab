class SharedKeyDictionary:

	def __init__(self):
		self.__dict = {}

	def add(self, key, value):
		self.__dict[key] = value

	def has_key(self, key):
		_key = ""

		for w in key:
			_key = _key + w

			if (_key in self.__dict):
				_key = ""

		return not _key






	