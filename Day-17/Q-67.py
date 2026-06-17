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

intersection = []
for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j] and arr1[i] not in intersection:
            intersection.append(arr1[i])

print("Intersection of arrays:")
for i in range(len(intersection)):
    print(intersection[i], end=" ")