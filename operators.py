
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
