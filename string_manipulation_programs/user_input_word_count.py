# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# Get user input a complete statement, print number of words in the input. (len() & .split/split())

user_input = input("Enter a complete statement: ")
word_count = len(user_input.split())

print(word_count)