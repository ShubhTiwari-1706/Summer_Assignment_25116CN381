def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [11, 12, 22, 25, 34, 64, 90] 
target = 25
result = binary_search(arr, target)
print(f"Element {target} found at index: {result}" if result != -1 else "Not found")