


class Node:
	def __init__(self, data, prevNode=None, nextNode=None):
		self.data = data
		self.nextNode = nextNode
		self.prevNode = prevNode

	def insert( self,  data ):


			if self.nextNode == None:
				self.nextNode = Node(  data )
				self.nextNode.prevNode = self
				return self.nextNode
			else:
				return self.nextNode.insert( data )


	def traverseForward( self ):
		if self==None:
			return

		print(self.data)
		if self.nextNode !=None:
			self.nextNode.traverse(  )


def traverseBackward( node ):
	if node == None:
		return

	print(node.data)
	if node.prevNode!=None:
		traverseBackward( node.prevNode )



def traverseForward( node ):
	if node == None:
		return

	print(node.data)
	if node.nextNode!=None:
		traverseForward(  node.nextNode )

head = Node(5)
head.insert( 23 )
tail = head.insert( 45)

#head.traverse()
traverseBackward( tail )