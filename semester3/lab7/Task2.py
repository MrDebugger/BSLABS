# Task 2
class StackList:
	def __init__(self,size):
		self.size = size
		self.List = []
	def push(self,elem):
		if len(self.List) == self.size:
			print("Stack is Full")
			return None
		self.List.append(elem)
		return elem
	def pop(self):
		if not len(self.List):
			print("Stack is Empty")
			return None
		return self.List.pop()
	def getTop(self):
		if not len(self.List):
			print("Stack is Empty")
			return None 
		return self.List[-1]
	def isEmpty(self):
		return bool(self.List)
	def isFull(self):
		if len(self.List) == self.size:
			return True
		return False
	def display(self):
		for data in self.List:
			print(data)


s2 = StackList(4)
for i in [1,7,5,2]:
	print("[+] Pushing",s2.push(i))
print("[+] Displaying:")
s2.display()
print("[-] Deleting Last Value:",s2.pop())
print("[+] Displaying:")
s2.display()
print("[+] Inserting element:",s2.push(9))
print("[+] Displaying:")
s2.display()
