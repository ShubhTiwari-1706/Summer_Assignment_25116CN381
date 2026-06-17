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

n3 = int(input("Enter size of third array: "))
arr3 = []
for i in range(n3):
    num = int(input())
    arr3.append(num)

common = []
for i in range(n1):
    for j in range(n2):
        for k in range(n3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k] and arr1[i] not in common:
                common.append(arr1[i])

print("Common elements:")
for i in range(len(common)):
    print(common[i], end=" ")
