class Item:
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue:
	def __init__(self):
		self.createQueue()

	def createQueue(self):
		self.head = None
		self.tail = None
		print("Queue created")

	def enqueue(self,item):
		item = Item(item)
		if not self.head:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item
		return True

	def dequeue(self):
		item = self.head.data
		self.head = self.head.next
		return item

	def isEmpty(self):
		return ("Yes","No")[bool(self.head)]

	def display(self):
		currentItem = self.head
		while currentItem:
			print(currentItem.data)
			currentItem = currentItem.next

q = Queue()
print("Queue is empty:",q.isEmpty())
print("Adding values 1, 7, 5, 2 ")
q.enqueue(1)
q.enqueue(7)
q.enqueue(5)
q.enqueue(2)
print("Displaying Queue items")
q.display()
print("removing two items at front")
q.dequeue()
q.dequeue()
print("Displaying Queue items")
q.display()
print("Insert new value 9")
q.enqueue(9)
print("Queue is empty:",q.isEmpty())
print("Displaying Queue items")
q.display()