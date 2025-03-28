# ask user input and suffix to check
user_input = input("Enter anything: ")
suffix = input("Enter suffix to check: ")

result = True # initializing resut

input_len = len(user_input)
suffix_len = len(suffix)

# determine if suffix is longer that input
if suffix_len > input_len:
    result = False
else:
    for i in range(suffix_len): # compare characters at the end
        if user_input[input_len - suffix_len + i] != suffix[i]:
            result = False
            break

# display result
print(result)