# Write a program to Convert binary to decimal.
binary = input("Enter a binary number: ")

decimal = 0
power = 0

# Right se left jaayenge
for i in range(len(binary) - 1, -1, -1):
    digit = int(binary[i])
    decimal = decimal + digit * (2 ** power)
    power += 1

print(f"Decimal of {binary} is: {decimal}")