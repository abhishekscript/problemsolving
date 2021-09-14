
from collections import OrderedDict
class Cache:
	def __init__(self, size):
		self.hashMap = OrderedDict({})
		self.size 	 = size
		self.ptr 	 = -1


	def add(self, key, value):
		
		self.hashMap[ key ] = value
		self.ptr +=1
		if self.ptr == self.size:
			self.hashMap.pop( list(self.hashMap.keys())[0] )
			self.ptr-=1

	def get(self, key):
		if self.hashMap.get(key) == None:
			raise ValueError

		self.hashMap.move_to_end(key)
		return self.hashMap[key]


	def __repr__(self):
		return f'{self.hashMap}'

lru = Cache( 5 )
lru.add(1,2)
lru.add(2,"A")
lru.add(3,"B")
lru.add(8,"9")
lru.add(4,"C")
lru.get(1)
lru.add(5,"D")
lru.add(6,"E")
lru.add(7,"F")

print( lru )
