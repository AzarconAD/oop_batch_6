# ask user input
user_input = input("Enter a phrase: ")

# convert the input to lowercase
user_input = user_input.lower()

# chop the phrase word by word
words = user_input.split()

# identify the first letter of the words
new_phrase = ""
for word in words:
    new_word = word[0].upper() + word[1:]
    new_phrase += new_word + " " # replace the case of the first letter of the words

# display output
print(new_phrase.strip())