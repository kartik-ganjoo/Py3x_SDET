# ===============================================================
#   Q3:
#       Factorial of a number
#       - eg. 5! = 5x4x3x2x1
#       - n! = n * (n-1) * (n-2) * ... * 2 * 1
#       - note: 0!=1, 1!=1, factorial for -ve num doesn't exist
#       - input -> +ve integer, 0 or above
#       - output -> factorial of the number
# ===============================================================

n = int(input("Enter a positive integer > "))
fact = 1

if (n==0) or (n==1):
    print(f"{n}! = {fact}")
elif n>=2:
    for i in range(1, n+1):
        fact = fact * i
    print(f"{n}! = {fact}")
else:
    print("Invalid input")
