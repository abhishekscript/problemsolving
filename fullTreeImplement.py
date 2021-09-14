class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def insert(self, data):

		if self.data > data:

			if self.left == None:
				self.left = Node( data )

			else:
				self.left.insert( data )

		elif self.data < data:

			if self.right == None:
				self.right = Node( data )

			else:
				self.right.insert( data )

	def __repr__(self):
		return f'{self.data}'

def height( node ):

	if node == None:
		return 0

	left = height(node.left)
	right = height(node.right)
	if left>right:
		return left+1
	else:
		return right+1


def preOrderTraversal( node ):
	if node == None:
		return

	print(node.data)
	preOrderTraversal( node.left )
	preOrderTraversal( node.right )

def inOrderTraversal( node ):
	if node == None:
		return

	postOrderTraversal( node.left )
	print(node.data)
	postOrderTraversal( node.right)

def postOrderTraversal( node ):
	if node == None:
		return

	postOrderTraversal( node.left )
	postOrderTraversal( node.right)	
	print(node.data)



def levelOrder( node, level, depth ):
	if node == None:
		return

	if level<depth:
		print(node.data)

	levelOrder( node.left, level+1, depth )
	levelOrder( node.right, level+1, depth)

levelMap = {}
def viewPrint( node, level, depth ):
	
	if node == None:
		return

	if level<depth:
		if level not in levelMap:
			print(node.data)
			levelMap[level] = [ node.data ]
		else:
			levelMap[level].append(node.data)
	viewPrint(node.left, level+1, depth)
	viewPrint(node.right, level+1, depth)
	
def invertTree( node ):
	if node == None:
		return

	#left, right = node.right, node.lef
	node.left , node.right = invertTree( node.right ), invertTree( node.left )
	return node

def isBalanced( node ):

	if node == None:
		return True

	left = height( node.left )
	right = height( node.right )

	return abs(left - right) <= 1 and isBalanced( node.left ) and isBalanced( node.right )


def isBST( node, left=None, right=None ):
	if node == None:
		return True

	if left!=None and left.data > node.data:
		return False

	if right!=None and right.data < node.data:
		return False

	return isBST( node.left, left, node ) and isBST(  node.right, node, right ) 


root = Node(2)
root.insert(1)
root.insert(3)
'''
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
'''
print(" PRE ORDER TRAVERSAL ")
preOrderTraversal( root )
print(" IN ORDER ")
inOrderTraversal( root )
print(" POST ORDER ")
postOrderTraversal( root )
print(" Level ORDER ")
levelOrder( root, 0, height(root) )
print(" LEFT VIEW  and GENERATE StateMap ")
viewPrint( root, 0, height(root) )
print(" StateMap ")
print( levelMap )



print(" INVERT TREE ")
invertTree( root )
print( isBST( root ) ,"is BST post inverted")

print(" PRE ORDER TRAVERSAL ")
preOrderTraversal( root )
print(" BALANCED ")
print( isBalanced( root ) )
print( isBST( root ) )

