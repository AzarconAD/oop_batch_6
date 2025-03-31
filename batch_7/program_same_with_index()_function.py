# ask user for input
user_input = input("Enter anything: ")

# ask what substring to find
substring = input("Enter a substring to find: ")

# ask where to start 
try:
    start = int(input("(Optional. Press enter to skip.) Where to start: ") or 0)
except ValueError:
    start = 0

# ask where to end
try:
    end = int(input("(Optional. Press enter to skip.) Where to end: ") or len(user_input))
except ValueError:
    end = len(user_input)

index = -1 # initializing the index
substring_len = len(substring)

# loop in the input to find the substring
for i in range(start, end - substring_len + 1):
    if user_input[i: i + substring_len] == substring:
        index = i # determine the index of the substring in the input
        break

# display the index
if index != -1:
    print(f"Index: {index}")
else:
    print("Not found")