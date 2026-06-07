# Write a program to Recursive sum of digits

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

n = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(n))