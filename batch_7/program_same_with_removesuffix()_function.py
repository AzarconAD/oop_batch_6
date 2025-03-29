# ask user for input and the suffix to remove
user_input = input("Enter anything: ")
suffix = input("Enter suffix to remove: ")

# check if there is a suffix in the input
if user_input.endswith(suffix):
    user_input = user_input[:len(user_input) - len(suffix)] # remove suffix
else:
    user_input = user_input

# display output
print(user_input)