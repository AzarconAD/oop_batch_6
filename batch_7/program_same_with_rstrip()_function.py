# ask for user inpt
user_input = input("Enter anything with trailing spaces: ")

# detect if there is trailing spaces
while user_input[-1] == " ":
    user_input = user_input[:-1] # remove trailing spaces

# display output
print(user_input)