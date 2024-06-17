# ===============================================================
#   Q2:
#       Triangle Classifier
#       - classify the triangle based on the length of sides
#           - Scalene => all sides different
#           - Isosceles => two equal sides
#           - Equilateral => all equal sides
#       - input -> side 1, side 2, side 3
#       - output -> Scalene/Isosceles/Equilateral
# ===============================================================

s1 = float(input("Enter a value for s1 > "))
s2 = float(input("Enter a value for s2 > "))
s3 = float(input("Enter a value for s3 > "))

if s1 == s2 == s3:
    print("It's an Equilateral Triangle.")
elif (s1==s2) or (s2==s3) or (s1==s3):
    print("It's an Isosceles Triangle.")
else:
    print("It's a Scalene Triangle.")