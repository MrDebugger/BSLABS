# Task 2
class Node:
	def __init__(self,value):
		self.data = value
		self.next = None 

	def has_value(self,value):
		"""Search for value in current Node"""
		return self.data == value


class Nodes:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self,node):
		"""Adding node to end of LinkedList (Nodes)"""
		if not isinstance(node,Node):
			node = Node(node)
		if self.head == None:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node


	def search_node(self,value):
		"""Searching Node in LinkedList (Nodes)"""
		current_node = self.head
		node_id = 1
		results = []
		while current_node:
			if current_node.has_value(value):
				results.append(node_id)
			current_node = current_node.next
			node_id += 1
		return results

	def update_node(self,position,value):
		"""Update Node in LinkedList (Nodes)"""
		current_node = self.head
		node_id = 1
		while current_node:
			if node_id == position :
				current_node.data = value
			current_node = current_node.next
			node_id += 1

	def delete_node(self,position):
		"""Delete Node in LinkedList (Nodes)"""
		current_node = self.head
		node_id = 1
		while current_node:
			if node_id+1 == position :
				current_node.next = current_node.next.next
			current_node = current_node.next
			node_id += 1

	def display(self,invert=False):
		"""Display all LinkedList (Nodes)"""
		current_node = self.head
		result = []
		while current_node:
			result.append(current_node.data)
			current_node = current_node.next
		if invert:
			result.reverse()
			return result
		return result
# Part 1
print("[+] Create Nodes")
n1 = Node('2')
n2 = Node('6')
n3 = Node('7')
n4 = Node('8')
n5 = Node('1')

nodes = Nodes()
for node in [n1,n2,n3,n4,n5]:
	nodes.add_node(node)
print("[+] Display all Nodes ")
print(', '.join(nodes.display()))

# Part 2
print("[+] Update Node at 3rd position having value 9")
nodes.update_node(3,'9')
print(', '.join(nodes.display()))

# Part 3
print("[+] Traverse the list forward")
print(', '.join(nodes.display()))
# Part 4
print("[+] Traverse the list backward")
print(', '.join(nodes.display(True)))
