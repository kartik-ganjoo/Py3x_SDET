# =====================================
#   Q1:
#       Right Triangle Star (*) pattern
#       - input => n
#       - if n=4, Output =>
#                   *
#                   **
#                   ***
#                   ****
# =====================================

n = int(input("Enter a number > "))

for i in range(1, n+1):
    print("*" * i)