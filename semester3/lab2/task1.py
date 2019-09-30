# Task 1:
def addMatrixes(m1,m2):
	finalMatrix = [[0,0,0],[0,0,0],[0,0,0]]
	print(finalMatrix)
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			finalMatrix[i][j] = m1[i][j] + m2[i][j]
	return finalMatrix

matrix1 = eval(input("Enter 2D Matrix1: "))
matrix2 = eval(input("Enter 2D Matrix2: "))
fMatrix = addMatrixes(matrix1,matrix2)
print(fMatrix)
