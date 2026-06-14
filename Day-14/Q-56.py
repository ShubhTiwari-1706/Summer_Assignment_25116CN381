a = [1, 0, 3, 0, 5]
non_zero = [x for x in a if x != 0]
zeros = [x for x in a if x == 0]
print(non_zero + zeros)