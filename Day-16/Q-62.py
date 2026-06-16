n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

max_count = 0
max_element = arr[0]

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j] == arr[i]:
            count = count + 1
    if count > max_count:
        max_count = count
        max_element = arr[i]

print("Element with maximum frequency:", max_element)
print("Frequency is:", max_count)