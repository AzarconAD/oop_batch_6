# ask user for input
user_input = input("Enter anything: ")

# ask what substring to find
substring = input("Enter a substring to find: ")

index = -1 # initializing the index
input_len = len(user_input)
substring_len = len(substring)

# loop in the input to find the substring
for i in range(input_len - substring_len + 1, -1, -1):
    if user_input[i: i + substring_len] == substring:
        index = i # determine the index of the substring in the input
        break

# display the index
if index != -1:
    print(f"Index: {index}")
else:
    print("Not found")