# ask user input
user_input = input("Enter anything: ")

swapped_string = ""
# identify each character's case using islower() and is upper()
for char in user_input: # manually swap case using lower() and upper()
    if char.islower():
        swapped_string += char.upper()  # Convert to uppercase
    elif char.isupper():
        swapped_string += char.lower()  # Convert to lowercase
    else:
        swapped_string += char

# print output
print(swapped_string)
