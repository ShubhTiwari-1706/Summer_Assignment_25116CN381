A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

n = len(A)
primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum = primary_sum + A[i][i]
    secondary_sum = secondary_sum + A[i][n - 1 - i]

print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)