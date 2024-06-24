#Program to determine if a given pattern matches a given word.
#Ntobeko Mhlongo
#26-04-2024

def match(pattern,word):
    if pattern == "" and word == "":#if the pattern and the word strngs are empty, they match
        return True
    elif pattern == "":#if the pattern string is empty, they don't match 
        return False
    elif pattern[0] == '*':#if the pattern starts with '*', recursively check if pattern[1:] matches word or word[1:]
        return match(pattern[1:], word) or (len(word) > 0 and match(pattern, word[1:]))
    elif pattern[0] == '?' or (len(word) > 0 and pattern[0] == word[0]):#if the pattern starts with '?' or matches the first character of word, recursively check the rest
        return match(pattern[1:], word[1:])
    else:
        return False

#To demonstrate, remove the first "#" in each of the following lines of code 
# print(match("h*llo", "hello"))  # True, '*' matches "e"
# print(match("h?llo", "hello"))  # False, '?' does not match "e"