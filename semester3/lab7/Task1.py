# Task 1
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

print("[+] Creating Stack of size 5")
s = StackList(5)
print("[+] Is Empty:",["No","Yes"][s.isEmpty()])
print("[+] Is Full:",["No","Yes"][s.isFull()])
print("[+] Pushing:",s.push(1))
print("[+] Pushing:",s.push(5))
print("[+] Pushing:",s.push(7))
print("[+] Poping:",s.pop())
print("[+] Pushing:",s.push(6))
print("[+] Pushing:",s.push(2))
print("[+] Pushing:",s.push(8))
print("[+] Is Empty:",["No","Yes"][s.isEmpty()])
print("[+] Is Full:",["No","Yes"][s.isFull()])
print("[+] Top Element:",s.getTop())
print("[+] Displaying Elements of Stack:")
s.display()
