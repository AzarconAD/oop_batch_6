# ask user for input
user_input = input("Enter anything: ")

# ask what substring to count
substring = input("Enter a substring to count: ")

# ask where to start
try:
    start = int(input("(Optional. Press enter to skip.) Where to start: " or 0))
except ValueError:
    start = 0

# ask where to end
try:
    end = int(input("(Optional. Press enter to skip.) Where to end: " or len(user_input)))
except ValueError:
    end = len(user_input)

count = 0 # initializing the count
string_len = len(user_input) 
substring_len = len(substring)

# loop through the input and check for the substring
for i in range(start, end - substring_len + 1):
    if user_input[i: i + substring_len] == substring:
        count += 1
    

# display output
print(count)