# Jordan Fitzgerald
# 4/7/2026
# Password Generator Project

import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
special_characters = string.punctuation

places = ["Atlanta", "Paris", "Tokyo", "Sydney", "New York", "Rome", "Barcelona", "Dubai", "Moscow", "Cape Town"]
foods = ["Pizza", "Sushi", "Burger", "Pasta", "Tacos", "Salad", "Steak", "Curry", "Dumplings", "Ice Cream"]
things = ["Guitar", "Camera", "Laptop", "Bicycle", "Backpack", "Watch", "Headphones", "Smartphone", "Book", "Pen"]
teams = ["Lakers", "Warriors", "Patriots", "Red Sox", "Yankees", "Cowboys", "Packers", "Steelers", "Celtics", "Mets"]

theme_words = places + foods + things + teams

# Get user input for password criteria
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower()
include_lowercase = input("Include lowercase letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
include_special = input("Include special characters? (y/n): ").lower() 
use_theme = input("Use a theme word? (y/n): ").lower()

# Build the character pool based on user choices
character_pool = ""
if include_uppercase == 'y':
    character_pool += uppercase_letters
if include_lowercase == 'y':
    character_pool += lowercase_letters
if include_numbers == 'y':
    character_pool += numbers
if include_special == 'y':
    character_pool += special_characters
if character_pool == "":
    print("No character types selected. Please select at least one type.")
    exit()

password =  ''
# Add a theme word if the user wants one
if use_theme == 'y':
    theme_word = random.choice(theme_words)
    character_pool += theme_word
while len(password) < length:
    password += random.choice(character_pool)

# Trim the password to the desired length
password = password[:length]
# Generate the password, but it cannot start with a special character or number
first_char_pool = character_pool
if include_special == 'y':
    first_char_pool = first_char_pool.replace(special_characters, '')
if include_numbers == 'y':
    first_char_pool = first_char_pool.replace(numbers, '')
password =  ''
for i in range(length):
    password += random.choice(character_pool)
    if i == 0:
        password = random.choice(first_char_pool) + password[1:]
    

# Check Password Strength
strength = "Weak"
if length >= 12 and include_uppercase == 'y' and include_lowercase == 'y' and include_numbers == 'y' and include_special == 'y':
    strength = "Strong"
elif length >= 8:
    strength = "Medium"

# Display the generated password
print(f"Generated Password: {password}")
print(f"Password Strength: {strength}")
