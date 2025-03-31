# ask user for input
user_input = input("Enter anything: ")

# ask the length of the output
length = int(input("How long should the output be?: "))

# add zeros in front of the input
num_zeros = length - len(user_input)
output = "0" * num_zeros + user_input

# display output
print(output)