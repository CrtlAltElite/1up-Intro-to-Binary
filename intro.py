# What is a Number System
# What is a Binary Number
# Why Do We Use Binary Numbers
# What is Memory
# What is a Byte and Nibble
# Why Do We Use Hexidecimal

# 0125 is 125 in base 10 same in base 2

#                                       * denotes 2^n 
print(bin(0))      # 0b 0
print(bin(1))      # 0b 1                    ^MAX bit
print(bin(2))      # 0b 10              *
print(bin(3))      # 0b 11
print(bin(4))      # 0b 100             *
print(bin(5))      # 0b 101
print(bin(6))      # 0b 110
print(bin(7))      # 0b 111
print(bin(8))      # 0b 1000            *
print(bin(9))      # 0b 1001
print(bin(15))     # 0b 1111                  ^MAX Nibble
print(bin(16))     # 0b 10000           *     
print(bin(32))     # 0b 100000          *
print(bin(64))     # 0b 1000000
print(bin(127))    # 0b 1111111          
print(bin(128))    # 0b 10000000        *
print(bin(255))    # 0b 11111111              ^MAX Byte
print(bin(256))    # 0b 100000000       *
print(bin(512))    # 0b 1000000000      *
print(bin(1023))   # 0b 111111111     
print(bin(1024))   # 0b 10000000000      *   
#  32 bits is 4 bytes
print(bin(2147483647)) #0b 0111 1111 1111 1111 1111 1111 1111 1111   ^Max in 32-bit signed
    #  Binary Literal Ob prefix 
# HeXidecimal Literal 0x prefix

print(hex(0))  #0x0
print(hex(10)) #0xa
print(hex(9))  #0x9
print(hex(15)) #0xf
print(hex(255)) #0xff



