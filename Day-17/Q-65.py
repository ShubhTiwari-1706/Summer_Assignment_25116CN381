n1 = int(input("Enter size of first array: "))
arr1 = []
for i in range(n1):
    num = int(input())
    arr1.append(num)

n2 = int(input("Enter size of second array: "))
arr2 = []
for i in range(n2):
    num = int(input())
    arr2.append(num)

merged = []
for i in range(n1):
    merged.append(arr1[i])
for i in range(n2):
    merged.append(arr2[i])

print("Merged array:")
for i in range(len(merged)):
    print(merged[i], end=" ")