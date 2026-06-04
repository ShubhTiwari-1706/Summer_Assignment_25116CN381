# Write a program to Generate Fibonacci series.
a = 0
b = 1

number = int(input('enter the number of terms in the fibonacci series : '))
print('fibonnaci series :')
for i in range (number):
    print(a , end =' ')
    
    c = b + a
    a = b
    b = c