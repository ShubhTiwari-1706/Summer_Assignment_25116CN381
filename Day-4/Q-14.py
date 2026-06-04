# Write a program to Find nth Fibonacci term.

nth = int(input("enter the nth term : "))

a = 0
b= 1

fibbo_series = []
for i in range (nth):
    fibbo_series.append(a)
    c = b + a
    a = b
    b = c

print(f'the {nth} th term of fibonacci series is {fibbo_series[i]}')
    