# Bitwise operations can be useful for performing certain mathematical
# problems faster and more efficiently than using conventional arithmetic operations. 
# Below are some common mathematical tasks where bitwise operations can come in handy:

# 1. Multiplication by 2:
# - Shift the bits to the left by one position.

n = 5
result = n << 1
print(result)  # Outputs: 10


# 2. Division by 2:
# - Shift the bits to the right by one position.
   
n = 10
result = n >> 1
print(result)  # Outputs: 5

# 3. Checking Odd or Even:
# - If the last bit is 1, the number is odd. If it's 0, the number is even.
   
n = 7
if n & 1:
    print("Odd")  # Outputs: Odd
else:
    print("Even")

# 4. Toggle a particular bit:
# - You can toggle a bit using the XOR operation.
   
# Toggle the 2nd bit (0-indexed) of number 5 (101 in binary)
n = 5
result = n ^ (1 << 2)
print(result)  # Outputs: 1 (001 in binary)

# 5. Turning off the rightmost 1-bit:
# - This can be useful in some algorithms (like ones dealing with subsets).
   
n = 6  # 110 in binary
result = n & (n - 1)
print(result)  # Outputs: 4 (100 in binary)

# 6. Checking if a number is a power of 2:
# - If a number `n` is a power of 2, then `n & (n - 1)` will be zero.
   
n = 16
if n & (n - 1) == 0:
    print("Power of 2")  # Outputs: Power of 2
else:
    print("Not a power of 2")

# 7. Swapping two numbers without a temporary variable:
# - Bitwise XOR can be used for this.
   
a = 5
b = 7
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # Outputs: 7 5

