"""
Program To prompt the user for an input string, count substrings starting with a consonant, 
print them along with the following 3 letters,and display the list of these substrings.

Ntobeko Mhlongo
"""

def generate_substrings(string):
    """
    Generate substrings of the input string that start with a consonant.

    Parameters:
        string (str): The input string.

    Returns:
        list: A list of substrings starting with a consonant.
    """
    consonants = 'bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  # Define consonants
    substrings = []  # List to hold the resulting substrings

    # Loop through the string to generate substrings of length 4
    for i in range(len(string) - 3):
        if string[i] in consonants:  # Check if the character is a consonant
            substrings.append(string[i:i+4])  # Append the substring of length 4 to the list
    
    return substrings

def count_substrings(string):
    """
    Count the substrings of the input string that start with a consonant and are of length 4.

    Parameters:
        string (str): The input string.

    Returns:
        int: The count of substrings matching the criteria.
    """
    consonants = 'bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  # Define consonants
    substrings_count = 0  # Initialize the counter for substrings

    # Loop through the string to count substrings of length 4
    for i in range(len(string) - 3):
        if string[i] in consonants:  # Check if the character is a consonant
            substrings_count += 1  # Increment the counter if the condition is met

    return substrings_count

def main():
    """
    Main function to accept input from the user, generate substrings, and count substrings starting with a consonant.
    """
    input_string = input("Enter a string:\n")
    input_string = input_string.lower()  # Convert input to lowercase for consistency
    
    substrings = generate_substrings(input_string)  # Generate substrings
    consonant_substring_count = count_substrings(input_string)  # Count substrings

    # Print the count of substrings
    print("Number of substrings of length 4 starting with a consonant:", consonant_substring_count)
    
    # Print the list of substrings
    print("Substrings of length 4 starting with a consonant:")
    if not substrings:
        print("[]")
    else:
        print(", ".join(substrings))

if __name__ == "__main__":
    main()