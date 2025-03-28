# ask user for input
user_input = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")

# identify the prefix using startswith()
if user_input.startswith(prefix):
    user_input = user_input[len(prefix):] # remove prefix

# display output
print(user_input)