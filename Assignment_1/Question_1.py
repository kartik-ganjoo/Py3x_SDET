# ===========================================================================
#   Q 1.1:
#       Explain the difference between "=" and "==" operator
#   A 1.1:
#       - "=" is the assignment operator, used to assign a value to a variable
#       - "==" is the equality operator, use to check a condition
# ===========================================================================

# "=" operator -> assignment operator
a = 5   # this will assign value 5 to variable a
print(a)

# "==" operator -> equal to
if a == 5:
    print("Matched!")

# ===========================================================================
#   Q 1.2:
#       What does "**" operator do?
#   A 1.2:
#       - "**" is the exponent/power operator
#       - e.g. 5**3 => this will give the value of 5 raised to the power of 3
# ===========================================================================

print(5**3)     # 5 x 5 x 5 = 125

# ===========================================================================
#   Q 1.3:
#       What does ^ do in python?
#   A 1.3:
#       - ^ refers to the bit XOR operator
#       - It will set each bit to 1 only if one of the two bits is 1
#           A B  Y
#           0 0  0
#           0 1  1
#           1 0  1
#           1 1  0
#       - e.g. 10 ^ 27 = 17
#               10 => 0  1  0  1  0
#               27 => 1  1  0  1  1
#                    ===============
#               17 => 1  0  0  0  1
# ===========================================================================

print(10^27)