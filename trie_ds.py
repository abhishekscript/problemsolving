from pprint import pprint
class Trie:
	def __init__(self):
		self.root = {"*":"*"}

	def add_word(self, word):

		curr_node = self.root
		for letter in word:
			if letter not in curr_node:
				curr_node[letter] = {}
			curr_node = curr_node[letter]
		curr_node["*"] = "*"

	def search_word(self, word):
		current_node = self.root
		for letter in word:
			print(letter)
			if letter in current_node:
				#print(self.root)
				current_node = current_node[letter]
				print(current_node)
			else:
				print(current_node)

	def __repr__(self):
		return f'{self.__dict__}'
	'''
	def does_word_exist(self, word):
		curr_node = self.root
		for letter in word:
			if letter not in curr_node:
				return False
	'''
obj = Trie()
obj.add_word( "hello" )
obj.add_word("hellboy")
obj.search_word("hellb")
#print(obj)
#pprint(obj)