# Write a program to Find largest prime factor.

number = int(input("enter number : "))

largest = 0
for i in range(2,number+1):
    if (number % i == 0):  
        
        is_prime = True
        for j in range(2, i):
            if (i % j == 0):
                is_prime = False
                break
        
        if (is_prime):
            largest = i

print("largest prime factor:", largest)