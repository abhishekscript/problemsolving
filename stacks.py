class Stack:
	def __init__(self, capacity):
		self.capacity = 3
		self.data = []
		self.index = 0

	def isUnderFlow(self):
		if self.index < 0:
			return True

		return False

	def isOverFlow(self):
		if self.index >= self.capacity:
			return True
 		
		return False

	def push( self, data ):

		if self.isOverFlow():
			print( "OverFlow")

		else:
			print("Added element {} at {}".format(data, self.index) )
			self.data.append(data)
			self.index+=1


	def pop(self):

		if self.isUnderFlow():
			print( "UnderFlow" )

		else:
			self.index-=1


	def display( self ):
		for x in range( self.index ):
			print( self.data[x] )


	#def detectCircular( self ):


# SAMPLE ENTRIES 

stackObject = Stack( 10 )
stackObject.push(1)
stackObject.push(5)
stackObject.push(7)

