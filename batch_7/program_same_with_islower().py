# ask user input 
user_input = input("Enter anything: ")

#check if input lowercase
def is_lower(string):
    for char in string:
        if "A" <= char <= "Z":
            return False
    return True

# display output
print(is_lower(user_input))