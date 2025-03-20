# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# Get user input fullname in incorrect casing, print in pascal case (use .replace to replace whitespace with "" and do similar thing to program 5.)

user_input = input("Enter your fullname: ").title()
remove_space = user_input.replace(" ", "")

print(remove_space)