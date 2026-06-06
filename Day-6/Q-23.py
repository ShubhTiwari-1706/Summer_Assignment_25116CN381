# Write a program to Count set bits in a number.
n = int(input("Enter a number: "))

num = n
count = 0

while num > 0:
    if num % 2 == 1:   
        count += 1
    num = num // 2     

print(f"Number of set bits in {n} is: {count}")