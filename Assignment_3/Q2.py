# =====================================
#   Q2:
#       Palindrome of a string
#       - input => string
#       - Output => True or False
# =====================================

def is_palindrome(input_string):
    reverse = ""
    for i in range(len(input_string)):
        reverse = input_string[i] + reverse

    if reverse == input_string:
        return True
    else:
        return False

s = str(input("Enter a string > "))

print(is_palindrome(s))

