class Node:
	def __init__(self, data, left=None, right=None):
		self.data  =  data
		self.left  =  left
		self.right =  right


	def insert(self, data):

			if self.data > data:
				if self.left == None:
					self.left = Node( data )
				else:
					self.left.insert(data)

			elif self.data < data:

				if self.right ==None:
					self.right = Node(data)

				else:
					self.right.insert(data)

def traverse( node ):
	if node==None:
		return

	
	print(node.data)
	traverse( node.left  )
	traverse( node.right )


def height( node ):
	if node == None:
		return 0

	left  = height(node.left)
	right = height(node.right)

	if left>right:
		left+=1
		return left
	else:
		right+=1
		return right


def levelPrint(node, level):
	
	if node==None:
		return

	if level == 1:
		print(node.data)

	elif level>1:
		levelPrint( node.left,  level-1 )
		levelPrint( node.right, level-1 )



def invert( node ):
	if node==None:
		return

	#print(node.data)

	node.left, node.right =  node.right , node.left
	invert(node.left)
	invert(node.right)
	#print(node.left.data, node.right.data   )


	#return node

# SAMPLE ENTRIES

root = Node(4)
for x in [2,7,1,3,6,9]:
	root.insert(x)
	#root.insert(6)
	#root.insert(3)
invert(root)
tree_height = height(root)

for x in range(1, tree_height+1):
	levelPrint( root, x )

#print( "before invert")
#traverse( root )

print( "post invert")

