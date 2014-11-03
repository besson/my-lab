from unittest import TestCase
from algos.shared_key_dict import SharedKeyDictionary

class TestSharedKeyDictionary(TestCase):

	def setUp(self):
		self.__skDict = SharedKeyDictionary()
		self.__skDict.add("super", "super")
		self.__skDict.add("hero", "spiderman")
		self.__skDict.add("hello", "world")
		self.__skDict.add("nature", "trees")

	def test_simple_double_key_ok(self):
		self.assertTrue(self.__skDict.has_key("superhero"))

	def test_simple_double_key_nok(self):	
		self.assertFalse(self.__skDict.has_key("superheroes"))

	def test_simple_single_key_ok(self):
		self.assertTrue(self.__skDict.has_key("super"))

	def test_simple_tripple_key_ok(self):
		self.assertTrue(self.__skDict.has_key("superheronature"))
