A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

result = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        total = 0
        for k in range(len(B)):
            total = total + A[i][k] * B[k][j]
        row.append(total)
    result.append(row)

print("Product of matrices:")
for row in result:
    print(row)