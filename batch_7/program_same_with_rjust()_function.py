# Ask for user input
user_input = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Check if the string is shorter than the width
if len(user_input) < width:
    spaces_needed = width - len(user_input) # Calculate how many spaces to add
    user_input = "-" * spaces_needed + user_input # Add spaces (Replaced with - to check) to the left of the string

# display output
print(user_input)