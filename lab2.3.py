# String Manipulation 3rd Question (Check if a string is a palindrome)

S = input("Enter a string: ")

# Removing spaces and converting to lowercase for comparison
cleaned_input = S.replace(" ", "").lower()

# Checking
is_palindrome = cleaned_input == cleaned_input[::-1]

# Output
if is_palindrome:
    print(S, "is a palindrome.")
else:
    print(S, "is not a palindrome.")