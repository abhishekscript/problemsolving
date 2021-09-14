


class Node:
	
	def __init__(self, data, nextNode=None):
		self.data = data
		self.nextNode = nextNode


def insert( node, data ):
	if node!=None:
		node.nextNode = Node( data )
		return node.nextNode

def display( node ):
	if node == None:
		return

	print(node.data)
	display( node.nextNode )


def reverse( node ):
	if node == None:
		return node

	if node.nextNode == None:
		return node

	headNode = reverse( node.nextNode )

	node.nextNode.nextNode = node
	node.nextNode = None

	return headNode


head=Node(1)
tail = insert( head, 3 )
tail = insert( tail, 4 )
tail = insert( tail, 2 )

display( head  )
print("\n")
head = reverse( head  )
display( head )