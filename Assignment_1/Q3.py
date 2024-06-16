# =====================================
#   Q3:
#       Compare two numbers
#       - input => 2 numbers, a and b
#       - output => a>b or a<b or a=b
# =====================================

a = float(input("Enter first number > "))
b = float(input("Enter second number > "))

if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
else:
    print("Both are equal.")