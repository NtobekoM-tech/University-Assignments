# Program to break up a sentence into a comma separeted list
# Ntobeko Mhlongo
# 20 March 2024
sentence = input("Enter a sentence:\n")

print("The word list:", end=" ") 
space = sentence.find(" ")
word_one = sentence[:space]# Slicing off the first word from the sentence
word_one = word_one[:].lower()# Making word one all lower case
print(word_one, end=", ")

for words in sentence[space+1:]:# Loop for the remaining words 
    if words == " ":
        print(",", end=" ")# If there is a space somewhere in the input, add a comma
    else:
        print(words.lower(), end="")# If there is no sace, print the words in lower case 
print(".")# At the end of the loop, print a full stop