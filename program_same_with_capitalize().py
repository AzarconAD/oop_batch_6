# ask user input
user_input = input("Enter anything: ").lower() # convert the input into lowercase


new_input = ""
if user_input[0].isalpha():           # identify the first letter
    new_input += user_input[0].upper() + user_input[1:]
else:
    new_input = user_input  # use upper() to convert the first letter into uppercase

# display output
print(new_input)