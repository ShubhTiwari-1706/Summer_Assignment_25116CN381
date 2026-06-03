# Write a program to Print prime numbers in a range.

range_1 = int(input('Enter the number from which you want the prime numbers : '))
range_2 = int(input('Enter the number upto which you want the prime numbers : '))

for i in range (range_1,range_2+1):
    if i<2:
        continue
    flag = 0
    for k in range(2,i):
        if i % k == 0:
            flag = 1
            break
    
    if flag == 0:
        print(i)
        

   
    
   
