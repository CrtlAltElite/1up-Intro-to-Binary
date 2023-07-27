
### 1. Bitwise AND (`&`):
# This takes two binary numbers and returns a new number 
# where each bit is set (1) if the corresponding bits in 
# the input numbers were both set (1), and cleared (0) otherwise.

#    1101  (decimal 13)
#  & 1011  (decimal 11)
#  --------
#    1001  (decimal 9)
print(13 & 11)
print(0b1101 & 0b1011)

# Identity Element: If A is any binary number, 
#   then A & 1...1 (a series of 1s of the same length as A) = A.
#   The binary number with all bits as 1 acts as the identity.

# Annihilator Element: A & 0...0 = 0...0 (for any A). 
#   The binary number with all bits as 0 will yield 0 
#   when AND-ed with any other number.

# Idempotent Property: A & A = A.

# Commutative Property: A & B = B & A.

# Associative Property: A & (B & C) = (A & B) & C.



### 2. Bitwise OR (`|`):
# This takes two binary numbers and returns a new number
# where each bit is set (1) if at least one of the corresponding bits
# in the input numbers was set (1).

#    1101  (decimal 13)
#  | 1011  (decimal 11)
#  --------
#    1111  (decimal 15)

print(13 | 11)
print(0b1101 | 0b1011)

# Identity Element: If A is any binary number, then A | 0...0 = A. 
#   The binary number with all bits as 0 acts as the identity.

# Annihilator Element: A | 1...1 = 1...1 (for any A). 
#   The binary number with all bits as 1 will yield 1s when OR-ed with any other number.

# Idempotent Property: A | A = A.

# Commutative Property: A | B = B | A.

# Associative Property: A | (B | C) = (A | B) | C.



### 3. Bitwise XOR (`^`):

# This takes two binary numbers and returns a new number
# where each bit is set (1) if exactly one of the corresponding bits
# in the input numbers was set (1). 
# If both bits are the same (both 1 or both 0), the result is 0.

#    1101  (decimal 13)
#  ^ 1011  (decimal 11)
#  --------
#    0110  (decimal 6)

print(13 ^ 11)
print(0b1101 ^ 0b1011)
# Identity Element: If A is any binary number, then A ^ 0...0 = A.

# Annihilator Element: There's no annihilator for XOR. 
#   XOR-ing with any constant value doesn't always result in a constant outcome.

# Idempotent Property: A ^ A = 0...0.

# Commutative Property: A ^ B = B ^ A.

# Associative Property: A ^ (B ^ C) = (A ^ B) ^ C.

# Inverse: The inverse of a bit under XOR is itself.
#   Meaning, if B is the inverse of A, then A ^ B = 0...0. 
#   But since A ^ A = 0...0, B must be equal to A.




### 4. Bitwise NOT (`~`):

#  This is a unary operation (meaning it takes a single input number)
#  and it inverts all the bits. 
#  Every bit that is set (1) is cleared (0) and vice versa.

#   ~1101   (decimal 13)
#  --------
#    0010 

# But due to two complement in python what we will actually get is ... -x-1
print(~0b1101)
print(-13-1)

# Inverse Property: If A is any binary number, then ~(~A) = A. 
# This means applying NOT twice brings you back to the original number.



### 5. Left Shift (`<<`):

#  This takes a binary number and shifts all its bits to the left by
#  a specified number of positions, filling in the rightmost bits with zeros.

#  Shifting `1101` (decimal 13) to the left by 1 position:

#    1101 << 1
#  --------
#    11010  (decimal 26)

print(13<<1)
print(0b1101<<1)

### 6. Right Shift (`>>`):

# This takes a binary number and shifts all its bits to the 
# right by a specified number of positions. 
# If the number is positive, the leftmost bits will be filled with zeros.

#  Shifting `1101` (decimal 13) to the right by 1 position:

#  1101 >> 1
#  --------
#    0110  (decimal 6)

print(13>>1)
print(0b1101>>1)


# Identity: Shifting by 0 doesn't change the number: A << 0 = A and A >> 0 = A.

# Associativity of Shift Amounts: (A << B) << C = A << (B + C) 
#   and (A >> B) >> C = A >> (B + C).

# Note: Shifting doesn't have a commutative property. 
#   For example, A << B is generally not the same as B << A.