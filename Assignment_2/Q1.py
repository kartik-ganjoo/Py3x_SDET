# ==============================================
#   Q1:
#       Leap Year Checker
#       - determine whether a given year is a leap year
#       - leap year occurs every 4 years i.e. input should be divisible by 4
#       - use if-else
#       - input -> 2024
# ==============================================

year = int(input("Enter a year > "))

if year % 4 == 0:
    print(f"{year} is a Leap Year!")
else:
    print(f"{year} is NOT a Leap Year.")