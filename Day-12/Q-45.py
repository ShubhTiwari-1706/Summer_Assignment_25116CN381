def is_palindrome(n):
    original = n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    return original == reversed_n

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")