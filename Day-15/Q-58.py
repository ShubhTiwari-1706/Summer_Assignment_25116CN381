a = [10, 20, 30, 40, 50]

total_sum = 0

for i in range(len(a)):
    total_sum = total_sum + a[i]

average = total_sum / len(a)

print("Sum:", total_sum)
print("Average:", average)