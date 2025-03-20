# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# Get user input fullname in incorrect casing, print in snake case (use .lower/lower() and .replace)

user_input = input("Enter your fullname: ").lower()
replace_space = user_input.replace(" ", "_")

print(replace_space)