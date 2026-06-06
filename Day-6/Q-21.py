#Write a program to Convert decimal to binary

n = int(input("enter a decimal number : "))

num = n
binary = ""

if n == 0:
    binary = "0"

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print(f"Binary of {n} is: {binary}")