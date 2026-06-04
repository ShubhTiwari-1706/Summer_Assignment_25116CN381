# Write a program to Print Armstrong numbers in a range.
range_1 = int(input('enter number from which you want armstrong numbers : '))
range_2 = int(input('enter number to which you want armstrong numbers : '))

for i in range(range_1,range_2+1):
    total = 0
    count = 0
    temp = i
    
    while (temp > 0):
        count += 1
        temp = temp // 10
    
    temp = i
    while (temp > 0):
        last_digit = temp % 10
        total += last_digit ** count
        temp = temp // 10
    
    if (total == i):
        print(i)