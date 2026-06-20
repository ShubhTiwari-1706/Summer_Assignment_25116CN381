A = [[1, 2, 3],
     [2, 5, 6],
     [3, 6, 9]]

n = len(A)
is_symmetric = True

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            is_symmetric = False

if is_symmetric == True:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")