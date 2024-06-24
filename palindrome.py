#Program to calcute if a string is a palindrome or not
#Ntobeko Mhlongo
#26-04-2024
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if len(s) == 0 or len(s) == 1:# If the string is empty or has a single digit, it is a palindrome 
        return True
    if s[0] != s[-1]:# If the first character is not the same as the last character, the string is not a palindrome
        return False
    return is_palindrome(s[1:-1])# Recursively checking if the middle part of the string is a palindrone
    
def main():
    s = input("Enter a string:\n")
    if is_palindrome(s) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

if __name__ == '__main__':
    main()

