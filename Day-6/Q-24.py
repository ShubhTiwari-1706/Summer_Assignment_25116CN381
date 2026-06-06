# Write a program to Find x^n without pow().
x = int(input("enter number: "))
n = int(input("enter power: "))

result = 1

for i in range(n):
    result = result * x

print(f"{x}^{n} = {result}")