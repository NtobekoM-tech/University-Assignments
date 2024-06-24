#Program to translate sentences to Pig Latin
#Ntobeko Mhlongo
#20 March 2024
sentence =  input("Enter a sentence:\n").lower()
vowel = 'aeiouAEIOU' # Assigning all vowels to the vowel variable

# Splitting the input sentence into words 
words = [] # Starting an empty list to store the words
word = '' # Starting an empty string to store characters of each word being processed 
for char in sentence: # Loop for each character in the input
    if char != " ": # If the character is not a space, the code appends the character to the word being processed if it is a space, the code checks if the 'word' is not empty
        word +=char
    elif word: # If it is  not empty, the code appends 'word' to the words list and resets 'word' back to an empty string
        words += [word]
        word =""
if word: # If there is a word left after the loop, the code appends it to the 'words' list
    words += [word]
    
pig_latin_sentence = "" # Variable to store translated words

for word in words: # Loop for every word on the 'words' list
    if word[0] in vowel: # If the first letter is a vowel, the code appends 'way' to the word
        pig_latin_word = word + "way"
    else: # If first letter is not a vowel, the code moves to the cosonent sequence
        consonant_sequence = ""
        for letter in word: # Loop for every letter until a vowel is found
            if letter in vowel:
                break # If the vowel is found, the code exits the loop
            consonant_sequence +=letter # Consonents are then added to the sequence
        pig_latin_word = word[len(consonant_sequence):] + "a" + consonant_sequence + "ay" # Appends pig latin translation for words starting with consonants
    pig_latin_sentence += pig_latin_word + " " # Appends translated word to the pig latin sentence
print(pig_latin_sentence)