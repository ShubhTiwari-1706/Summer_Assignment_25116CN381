arr = [10, 25, 3, 47, 8]
target = 47
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")