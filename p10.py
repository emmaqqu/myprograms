# String stuff

def is_palindrome(word):
    # checks if argument word is a palindrome
    return word == word[::-1]

text = input("Enter a word: ")
if is_palindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is boring")