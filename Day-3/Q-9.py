# Write a program to Check whether a number is prime
flag = 0
number = int(input('Enter a number : '))

for i in range (2,number):
    if number % i == 0:
        flag = 1
        break
    
if flag == 1:
    print(f'{number} is not a prime number')
else:
    print(f'{number} is a prime number')
