A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

transpose = []
for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    transpose.append(row)

print("Transpose of matrix:")
for row in transpose:
    print(row)