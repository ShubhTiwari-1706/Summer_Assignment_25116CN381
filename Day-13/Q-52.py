arr = [1, 2, 3, 2, 4, 3, 5]
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            if arr[i] not in duplicates:
                duplicates.append(arr[i])

print("Duplicate elements are:", duplicates)