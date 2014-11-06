# Print all string combinations

class Node:

	def __init__(self, key):
		self._key = key
		self._right = None
		self._left = None

	def add_right(self, node):
		self._right = node

	def add_left(self, node):
		self._left = node

	def right(self):
		return self._right

	def left(self):
		return self._left

	def key(self):
		return self._key


class StringCombinations:

	def __init__(self, _input):
		self._result = []
		self._roots = _input.pop(0)
		self._input = _input


	def print_all(self):
		for key in self._roots:
			_input = [i for i in self._input]
			tree = self._build_tree(Node(key), _input)
			self._print_tree(tree, key)

		return self._result

	def _print_tree(self, root, string):
		if (root and (root.left() is None and root.right() is None)):
			self._result.append(string)
		else:
			self._print_tree(root.right(), "%s %s" % (string, root.right().key())) 
			self._print_tree(root.left(), "%s %s" % (string, root.left().key()))

	def _build_tree(self, node, _input):
		if (len(_input) == 0):
			return node

		keys = _input[0]

		right = self._build_tree(Node(keys[0]), _input[1:len(_input) + 1])
		left = self._build_tree(Node(keys[1]), _input[1:len(_input) + 1])

		node.add_right(right)
		node.add_left(left)

		return node