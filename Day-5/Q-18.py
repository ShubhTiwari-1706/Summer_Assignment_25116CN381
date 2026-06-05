# Write a program to Check strong number.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

number = int(input("enter number : "))

temp = number
sum = 0

while (temp > 0):
    last_digit = temp % 10
    sum = sum + factorial(last_digit) 
    temp = temp // 10

if (sum == number):
    print(number, "is a strong number")
else:
    print(number, "is not a strong number")
            
