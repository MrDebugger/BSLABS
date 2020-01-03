class Node:
	def __init__(self,data):
		self.data = data
		self.nextNode = None
		
class Queue:
	def __init__(self):
		self.createQueue()
	def createQueue(self):
		self.head = None
		self.tail = None

	def enQueue(self,node):
		node = Node(node)
		if not self.head:
			self.head = node
		else:
			self.tail.nextNode = node
		self.tail = node

	def deQueue(self):
		node = self.head.data
		self.head = self.head.nextNode
		return node

	def isEmpty(self):
		if self.head:
			return False
		else:
			return True

	def display(self):
		datas = []
		currentNode = self.head
		while currentNode:
			datas.append(currentNode.data)
			currentNode = currentNode.nextNode
		return datas