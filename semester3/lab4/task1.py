# Task 1
class Node:
	def __init__(self,value):
		self.data = value
		self.nextNode = None 

	def hasValue(self,value):
		"""Search for value in current Node"""
		return self.data == value

	def getData(self):
		"""Returns current node data"""
		return self.data

	def getNextNode(self):
		"""Returns next node in the current node"""
		return self.nextNode

	def setNextNode(self,node):
		"""Set Next node for the current node"""
		self.nextNode = node
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
		currentNode = self.head
		nodeId = 1
		while currentNode:
			if nodeId+1 == position :
				newNode = node
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
			self.head.nextNode
			return True
		currentNode = self.head
		nodeId = 1
		deleted = False
		while currentNode:
			if nodeId == position :
				currentNode.nextNode = currentNode.nextNode.nextNode
				self.size -= 1
				deleted = True
			currentNode = currentNode.nextNode
			nodeId += 1
		return deleted

	def displayNodes(self,invert=False):
		"""Display all LinkedList (Nodes)"""
		currentNode = self.head
		result = []
		while currentNode:
			result.append(currentNode.data)
			currentNode = currentNode.nextNode
		if invert:
			result.reverse()
			return result
		return result
# Part 1
print("[+] Create Nodes")
inputNodes = []
while True:
	nodeValue = input("[>] Add node value [(E)nter to exit adding]: ")
	if nodeValue.lower()[0] == 'e':
		break
	node = Node(nodeValue)
	inputNodes.append(node)


nodes = Nodes()
i = 0
for node in inputNodes:
	nodes.addNode(node)
	i+=1
	print(f"Node at Address {hex(id(node))} is added to Nodes at position {i}.")

# Part 2
print("\n[+] Inserting Nodes at a Specific Position")
while True:
	try:
		nodePosition = int(input("[>] Enter Position of the Node: "))
	except:
		print("[-] Please Enter Numbers only.")
	finally:
		nodeValue = input("[>] Enter Value of the Node: ")
		node = Node(nodeValue)
		nodes.insertNode(nodePosition,node)
		print(f"[+] Node Inserted at Address {hex(id(node))} at position {nodePosition}")
		break

# Part 3
print("\n[+] Deleting node at Specific Position")
while True:
	try:
		nodePosition = int(input("[>] Enter Node Position to delete Node: "))
	except:
		print("[-] Please enter Numbers only")
	finally:
		if nodes.deleteNode(nodePosition):
			print(f"[+] Node deleted at position {nodePosition}")
		else:
			print(f"[-] No Node found at position {nodePosition}")
		break


# Part 4
print("\n[+] Printing all the data of the Nodes")
print(", ".join(nodes.displayNodes()))


# Part 5
print("\n[+] Find Specific Node")
nodeValue = input("[>] Enter value of the node to find: ")
foundNodes = nodes.searchNode(nodeValue)
if foundNodes:
	print(f"[+] The following nodes found to have the value {nodeValue}: {', '.join(foundNodes)}")
else:
	print(f"[-] No node found to have the value {nodeValue}")
