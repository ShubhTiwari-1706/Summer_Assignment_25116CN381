def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input('enter number : '))
b = int(input('enter number : '))

print(find_maximum(a,b))