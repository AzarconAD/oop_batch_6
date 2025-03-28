# ask user for input
user_input = input("Enter anything with leading spaces: ")
no_lead_spaces = ""

found_char = False
for char in user_input: # detect if there is leading spaces in the input
    if char != " " and not found_char: 
        found_char = True
    if found_char:
        no_lead_spaces += char
       
# display
print(no_lead_spaces)