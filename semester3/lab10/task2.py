# Task 2
# a. Read the elements of a list with n int elements. 
def checkInt(elements):
	for element in elements:
		if element.__class__ == int:
			print(element)

# b. Functions to calculate the sum, product of a list. 
def sum(elements):
	add = 0
	for element in elements:
		if element.__class__ == int:
			add+=element
	return add
def product(elements):
	mul = 1
	for element in elements:
		if element.__class__ == int:
			mul*=element
	return mul

# c. Function to calculate the maximum and its position.
def maximum(elements):
	max = elements[0]
	index = 0
	for element in elements:
		if element.__class__ == int:
			if max < element:
				max = element
	return max,elements.index(max)

# d. Function to find if an element x belongs to a list.	 
def inList(element,elements):
	return element in elements

elements = [1,2,'3',5,'1',6,9]
print("List:")
print(elements)
print("Check Integers:")
checkInt(elements)
print("Sum:")
print(sum(elements))
print("Product:")
print(product(elements))
print("Maximum (element, index):")
print(maximum(elements))
print("2 in List:")
print(inList(2,elements))
