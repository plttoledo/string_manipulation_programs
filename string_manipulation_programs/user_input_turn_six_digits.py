# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
# Get user input from 0-1000, output 6 digits with zeros at the beginning that completes 6 digits.

user_input = int(input("Enter a number from 0-1000: "))

if 0 <= user_input <= 1000:
    six_digits = f"{user_input:06d}"
    print(six_digits)

else:
    print("Invalid input! Please input a number from 0-1000 only.")
