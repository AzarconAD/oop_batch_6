# ask user input and the preffix to check
user_input = input("Enter anything: ")
prefix = input("Enter prefix to check: ")

result = True

input_len = len(user_input)
prefix_len = len(prefix)

if prefix_len > input_len:
    result = False
else:
    for i in range(prefix_len): # compare input and prefix at the start
        if user_input[i] != prefix[i]:
            result = False
            break

# display result
print(result)