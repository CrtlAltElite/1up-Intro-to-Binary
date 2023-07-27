# Bitwise AND (&):
# Use Case: Extracting specific color channels from an RGBA pixel.

# pixel = 0xFF34A2BC  # This is an RGBA color, where R=FF, G=34, B=A2, A=BC.
# RED_MASK = 0xFF000000
# BLUE_MASK = 0x0000FF00
# # Extract the red channel:
# red_channel = (pixel & RED_MASK) >> 24  # 0xFF
# print(hex(red_channel))
# blue_channel = (pixel & BLUE_MASK) >> 8  # 0xa2
# print(hex(blue_channel))

# Red: bits 24-31
# Green: bits 16-23
# Blue: bits 8-15
# Alpha: bits 0-7
# The value 0xFF34A2BC is broken down as:

# Red (RR) = 0xFF (bits 24-31)
# Green (GG) = 0x34 (bits 16-23)
# Blue (BB) = 0xA2 (bits 8-15)
# Alpha (AA) = 0xBC (bits 0-7)





# # Bitwise OR (|):
# READ, WRITE, EXECUTE = 1, 2, 4

# # Grant READ and EXECUTE permissions
# permissions = READ | EXECUTE  # 1 | 4 = 5
# print(permissions)




# Bitwise XOR (^)
# Finding a number that appears only once in a list while other numbers appear twice

# def find_unique_number(arr):
#     result = 0
#     for num in arr:
#         print(f'{result}^{num}', {result^num})
#         result ^= num
#     return result

# nums = [4, 2, 4, 6, 2, 5, 5]
# print(find_unique_number(nums))  # Outputs 6



# # Bitwise NOT (~):
# # Use Case: Inverting a binary flag.
# # Feature Flags
# FEATURE_A = 0b0001
# FEATURE_B = 0b0010
# FEATURE_C = 0b0100
# FEATURE_D = 0b1000

# # Current configuration: All features enabled
# config = FEATURE_A | FEATURE_B | FEATURE_C | FEATURE_D  # 0b1111

# # Now, let's say due to some runtime conditions, you want to disable FEATURE_B. 
# # This is where bitwise NOT (~) is handy.
# config &= ~FEATURE_B

# print(bin(config))  # Outputs: 0b1101


# # Pack two 16-bit numbers into one 32-bit number
# def pack_numbers(a, b):
#     return (a << 16) | b

# # Unpack the 32-bit number back into two 16-bit numbers
# def unpack_numbers(x):
#     return (x >> 16) & 0xFFFF, x & 0xFFFF

# packed = pack_numbers(65535, 12345)
# print(bin(packed))
# a, b = unpack_numbers(packed)
# print(a, b)  # Outputs: 65535 12345