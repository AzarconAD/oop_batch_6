# Ask for user input
user_input = input("Enter anything: ")
width = int(input("Enter the total width: "))

# determine the spaces needed to center the input
total_spaces = width - len(user_input)

# Check if the string length is less than the width
if total_spaces > 0:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    user_input = " " * left_spaces + user_input + " " * right_spaces
    
# display output
print(user_input)