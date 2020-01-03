class Node:
	def __init__(self, data):
		self.data = data
		self.leftNode = None
		self.rightNode = None
	def insertNode(self, data):
		if data < self.data:
			if self.leftNode:
				return self.leftNode.insertNode(data)
			else:
				self.leftNode = Node(data)
		else:
			if self.rightNode:
				return self.rightNode.insertNode(data)
			else:
				self.rightNode = Node(data)
				
	def findNode(self, data):
		if self.data == data:
			return True
		elif data < self.data and self.leftNode:
			return self.leftNode.findNode(data)
		elif data > self.data and self.rightNode:
			return self.rightNode.findNode(data)
		return False

	def preorder(self, List):
		List.append(self.data)
		if self.leftNode:
			self.leftNode.preorder(List)
		if self.rightNode:
			self.rightNode.preorder(List)
		return List
	def postorder(self, List):
		if self.leftNode:
			self.leftNode.postorder(List)
		if self.rightNode:
			self.rightNode.postorder(List)
		List.append(self.data)
		return List
	def inorder(self, List):
		if self.leftNode:
			self.leftNode.inorder(List)
		List.append(self.data)
		if self.rightNode:
			self.rightNode.inorder(List)
		return List

class BinarySearchTree:
	def CreateTree(self):
		self.root = None
	def insertNode(self, data):
		if self.root:
			self.root.insertNode(data)
		else:
			self.root = Node(data)

	def searchNode(self, data):
		return self.root.findNode(data)
		
	def preOrder(self):
		return self.root.preorder([])
		
	def postOrder(self):
		return self.root.postorder([])

	def inOrder(self):
		return self.root.inorder([])

