a = [1, 2, 3, 4, 5, 6, 7, 8]

even_count = 0
odd_count = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even elements count:", even_count)
print("Odd elements count:", odd_count)