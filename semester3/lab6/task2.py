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

	def setData(self,data):
		"""Returns current node data"""
		self.data = data
		return True

	def getNextNode(self):
		"""Returns next node in the current node"""
		return self.nextNode

	def getPrevNode(self):
		"""Returns prev node in the current node"""
		return self.prevNode

	def setNextNode(self,node):
		"""Set Next node for the current node"""
		self.nextNode = node
		return True

	def setPrevNode(self,node):
		"""Set prev node for the current node"""
		self.prevNode = node
		return True

class Nodes:
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self,node):
		"""Adding node to end of LinkedList (Nodes)"""
		if not isinstance(node,Node):
			node = Node(node)
		if self.head == None:
			self.head = node
		else:
			node.setPrevNode(self.tail)
			self.tail.setNextNode(node)
		self.tail = node
		# CLL
		self.tail.setNextNode(self.head)
		self.head.setPrevNode(self.tail)

	def searchNode(self,value):
		"""Searching Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		results = []
		while currentNode:
			if currentNode.hasValue(value):
				results.append(str(nodeId))
			# To Stop CLL infinite recursion
			if currentNode == self.tail:
				break
			currentNode = currentNode.getNextNode()
			nodeId += 1
		return results

	def updateNode(self,position,value):
		"""Update Node in LinkedList (Nodes)"""
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId+1 == position :
				currentNode.setData(value)
			# To Stop CLL infinite recursion
			if currentNode == self.tail:
				break
			currentNode = currentNode.getNextNode()
			nodeId += 1

	def insertNode(self,position,node):
		"""Insert node at a Specific Position"""
		if not isinstance(node,Node):
			node = Node(node)
		if position == 1:
			self.head.setPrevNode(node)
			node.setNextNode(self.head)
			self.head = node
			self.head.setPrevNode(self.tail)
			return
		elif position == -1:
			self.tail.setNextNode(node)
			node.setPrevNode(self.tail)
			self.tail = node
			self.tail.setNextNode(self.head)
			return
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId+1 == position :
				newNode = node
				newNode.setPrevNode(currentNode)
				newNode.setNextNode(currentNode.getNextNode())
				currentNode.setNextNode(newNode)
			# To Stop CLL infinite recursion
			if currentNode == self.tail:
				break
			currentNode = currentNode.getNextNode()
			nodeId += 1

	def deleteNode(self,position):
		"""Delete Node in LinkedList (Nodes)"""
		if position == 1:
			self.head = self.head.getNextNode()
			self.head.setPrevNode(self.tail)
			return True
		elif position == -1:
			self.tail = self.tail.getPrevNode()
			self.tail.setNextNode(self.head)
			return True
		currentNode = self.head
		nodeId = 1
		deleted = False
		while currentNode:
			if nodeId+1 == position :
				currentNode.setNextNode(currentNode.getNextNode().getNextNode())
				currentNode.setPrevNode(currentNode.getNextNode().getPrevNode())
				deleted = True
			# To Stop CLL infinite recursion
			if currentNode == self.tail:
				break
			currentNode = currentNode.getNextNode()
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
			result.append(currentNode.getData())
			# to stop infinite recursion
			if (currentNode == self.tail and not invert) or ( currentNode == self.head and invert ):
				break
			if not invert:
				currentNode = currentNode.getNextNode()
			else:
				currentNode = currentNode.getPrevNode()
		return result

# Part 1
print("[+] Create Nodes")
nodes = Nodes()
for node in ['9','5','4','3','2','1']:
	nodes.addNode(node)
print("[+] Nodes Created")

# Part 2
print("[+] Displaying nodes Both Ways")
print("[+] Ascending Order")
print(', '.join(nodes.displayNodes()))
print("[+] Descending Order")
print(', '.join(nodes.displayNodes(invert=True)))

# Part 3
print("\n[+] Insert Node at Last position having value 9")
nodes.insertNode(-1,'9')
print(', '.join(nodes.displayNodes()))

# Part 4
print("\n[+] Search Nodes having value 9 and 12")
for value in ['9','12']:
	foundNodes = nodes.searchNode(value)
	if foundNodes:
		print(f"[+] Nodes having value {value} are:",', '.join(foundNodes))
	else:
		print(f"[-] No Node found having value {value}")

# Part 5
print("\n[+] Delete last Node and display all Values")
nodes.deleteNode(-1)
print("[+] Node Deleted")
print(', '.join(nodes.displayNodes()))
