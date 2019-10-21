# Task 2
class Node:
	def __init__(self,value):
		self.data = value
		self.nextNode = None 
		self.prevNode = None 

	def hasValue(self,value):
		"""Search for value in current Node"""
		return self.data == value

	def getData(self):
		"""Returns current node data"""
		return self.data

	def getNextNode(self):
		"""Returns next node in the current node"""
		return self.nextNode

	def getPrevNode(self):
		"""Returns next node in the current node"""
		return self.prevNode

	def setNextNode(self,node):
		"""Set Next node for the current node"""
		self.nextNode = node
		return True

	def setPrevNode(self,node):
		"""Set Next node for the current node"""
		self.prevNode = node
		return True

class Nodes:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def addNode(self,node):
		"""Adding node to end of LinkedList (Nodes)"""
		if not isinstance(node,Node):
			node = Node(node)
		if self.head == None:
			self.head = node
		else:
			node.prevNode = self.tail
			self.tail.nextNode = node
		self.tail = node
		self.size += 1

	def searchNode(self,value):
		"""Searching Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		results = []
		while currentNode:
			if currentNode.hasValue(value):
				results.append(str(nodeId))
			currentNode = currentNode.nextNode
			nodeId += 1
		return results

	def updateNode(self,position,value):
		"""Update Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId == position :
				currentNode.data = value
			currentNode = currentNode.nextNode
			nodeId += 1

	def insertNode(self,position,node):
		"""Insert node at a Specific Position"""
		if not isinstance(node,Node):
			node = Node(node)
		if position == 1:
			self.head.prevNode = node
			node.nextNode = self.head
			self.head = node
			self.size+=1
			return
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId+1 == position :
				newNode = node
				newNode.prevNode = currentNode
				newNode.nextNode = currentNode.nextNode
				currentNode.nextNode = newNode
				self.size += 1
			currentNode = currentNode.nextNode
			nodeId += 1

	def getSize(self):
		"""Return Size of Nodes"""
		return self.size

	def deleteNode(self,position):
		"""Delete Node in LinkedList (Nodes)"""
		if position == 1:
			self.head = self.head.nextNode
			self.head.prevNode = None
			self.size+=1
			return True
		currentNode = self.head
		nodeId = 1
		deleted = False
		while currentNode:
			if nodeId == position :
				currentNode.nextNode = currentNode.nextNode.nextNode
				currentNode.prevNode = currentNode.nextNode.prevNode
				self.size -= 1
				deleted = True
			currentNode = currentNode.nextNode
			nodeId += 1
		return deleted

	def displayNodes(self,invert=False):
		"""Display all LinkedList (Nodes)"""
		if not invert:
			currentNode = self.head
		else:
			currentNode = self.tail
		result = []
		while currentNode:
			result.append(currentNode.data)
			if not invert:
				currentNode = currentNode.nextNode
			else:
				currentNode = currentNode.prevNode
		return result
# Part 1
print("[+] Create Nodes")

nodes = Nodes()
for node in ['2','6','7','8','1']:
	nodes.addNode(node)
print(', '.join(nodes.displayNodes()))

# Part 2
print("\n[+] Insert Node at 3rd position having value 9")
nodes.insertNode(3,'9')
print(', '.join(nodes.displayNodes()))

# Part 3
print("\n[+] Search Nodes having value 9 and 12")
for value in ['9','12']:
	foundNodes = nodes.searchNode(value)
	if foundNodes:
		print(f"[+] Nodes having value {value} are:",foundNodes)
	else:
		print(f"[-] No Node found having value {value}")

# Part 4
print("\n[+] Delete 3rd Node and display all Values")
nodes.deleteNode(3)
print("[+] Node Deleted")
print(', '.join(nodes.displayNodes()))
