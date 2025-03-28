# ask user input
user_input = input("Enter anything: ")
# check each character if lowercase or uppercase
def is_upper(string):
    for char in string:
        if "a" <= char <= "z":
            return False
    return True
# display result
print(is_upper(user_input))