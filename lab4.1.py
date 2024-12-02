string = input("Enter a sentence: ")
words = string.lower().split()
palindrome_count = sum(1 for word in words if word == word[::-1])
print(f"Number of palindrome words: {palindrome_count}")
