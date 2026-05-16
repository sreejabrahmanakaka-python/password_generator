import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters   # a-z, A-Z
    if use_numbers:
        characters += string.digits          # 0-9
    if use_symbols:
        characters += string.punctuation     # !@#$%

    if characters == "":
        return "Please select at least one character type!"

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


# ---- User Input ----
print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

letters = input("Include letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

# ---- Generate Password ----
result = generate_password(length, letters, numbers, symbols)

print("\nGenerated Password:", result)