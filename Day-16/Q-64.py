n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

result = []

for i in range(n):
    present = 0
    for j in range(len(result)):
        if result[j] == arr[i]:
            present = 1
    if present == 0:
        result.append(arr[i])

print("Array after removing duplicates:")
for i in range(len(result)):
    print(result[i], end=" ")
