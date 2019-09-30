# Task 3
m, n = [int(k) for k in input("Enter (Rows[Space]Columns) i.e: 3 4: ").split()]
A = [[int(k) for k in input('Enter a row'+str(i+1)+' i.e '+'1 '*n+': ').split()] for i in range(m)]
c = int(input('Enter an Integer: '))

for i in range(m):
    for j in range(n):
        A[i][j] *= c

print('\n'.join([' '.join([str(k) for k in row]) for row in A]))
