# Write a program to Find GCD of two numbers.

num_1 = int(input('enter first number : '))
num_2 = int(input('enter second number : '))

list_1=[]
for i in range(1,num_1+1):
    if num_1 % i == 0:
        list_1.append(i)
list_2=[]
for i in range(1,num_2+1):
    if num_2 % i == 0:
        list_2.append(i)

list_1 =set(list_1)
list_2 =set(list_2)

gcd =(max(list_1.intersection(list_2)))

print(f'the GCD of {num_1} and {num_2} is {gcd}')