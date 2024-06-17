# ===============================================================
#   Q4:
#       Fibonacci series for n elements
#       - sequence = 0 1 1 2 3 5 8 13 21 34 55 ...
#       - n_th element = (n-1) + (n-2)
#       - first two elements will always be 0 and 1 resp.
# ===============================================================

n = int(input("Enter a positive integer > "))

# Solution 1
fibo = []

for i in range(n):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    else:
        fibo.append(fibo[-1] + fibo[-2])

print("Using Soln 1: ", fibo)

# Solution 2
n1, n2 = 0, 1   # first two elements of the series
count = 0

print("Using Soln 2: ")
while count < n:
    if count == 0:
        n_th = n1
    elif count == 1:
        n_th = n2
    else:
        n_th = n1 + n2
        n1 = n2
        n2 = n_th
    count += 1
    print(n_th)
