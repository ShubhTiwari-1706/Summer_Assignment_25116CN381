# Write a program to Check Armstrong number.

number = int(input('enter number : '))
number_1 = number
number_2 = number

count = 0
while (number > 0):
    count += 1 
    number = number // 10

total  = 0
while (number_1 > 0):
    last_digit = number_1 % 10
    total = total + last_digit**count
    number_1 = number_1 // 10
    
if total == number_2:
    print(f'{number_2} is an armstrong number')
else:
    
    print(f'{number_2} is not an armstrong number')