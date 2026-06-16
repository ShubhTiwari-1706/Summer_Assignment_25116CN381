n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

total = n + 1

expected_sum = total * (total + 1) // 2

actual_sum = 0
for i in range(n):
    actual_sum = actual_sum + arr[i]

missing = expected_sum - actual_sum

print("Missing number is:", missing)