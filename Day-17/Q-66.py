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

union = []
for i in range(n1):
    if arr1[i] not in union:
        union.append(arr1[i])

for i in range(n2):
    if arr2[i] not in union:
        union.append(arr2[i])

print("Union of arrays:")
for i in range(len(union)):
    print(union[i], end=" ")