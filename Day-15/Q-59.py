a = [10, 25, 3, 47, 8, 15]

largest = a[0]
smallest = a[0]

for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
    if a[i] < smallest:
        smallest = a[i]

print("Largest element:", largest)
print("Smallest element:", smallest)