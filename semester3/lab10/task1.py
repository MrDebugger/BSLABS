# Task 1
class Queue:
	# a. Create Empty List
	def __init__(self):
		self.list = []
	# b. List is Empty or Not
	def isEmpty(self):
		return ('Yes','No')[bool(self.list)]
	# c. Add number at index 0
	def enqueue(self,number):
		if number not in self.list:
			self.list.insert(0,number)
			return True
		return False
	# d. Remove the number
	def dequeue(self):
		if len(self.list)>0:
			return self.list.pop()
		return "Queue is Empty"
	# print size of list
	def size(self):
		return len(self.list)
		
# Object Creation and running of the above tasks 
Q = Queue()
print(Q.isEmpty())
print(Q.enqueue(1))
print(Q.enqueue(5))
print(Q.enqueue(7))
print(Q.isEmpty())
print(Q.dequeue())
print(Q.dequeue())
print(Q.size())
print(Q.dequeue())