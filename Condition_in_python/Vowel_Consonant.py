char = input("Enter a character: ")
if char in "aeiouAEIOU":
    print("The character is vowel")
elif char in"@#$%^&*()":
    print("This is a Special Character.")
else:
    print("The character is consonant.")