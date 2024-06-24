# Program to find the number of substrings that begin with a given character from the given string and prints those substrings.
# Ntobeko Mhlongo

def count_substrings(main_string, char):
    """
    Function to count the occurrences of substrings starting with a certain character in a given string.

    Args:
    main_string (str): The main string in which occurrences will be counted.
    char (str): The character to check for at the beginning of substrings.

    Returns:
    int: The count of substrings starting with the specified character.
    """
    occurrences = 0  # Initialize the counter for occurrences
    length = len(char)  # Get the length of the substring to be matched
    
    # Iterate over the main string with a range that allows full substring comparison
    for i in range(len(main_string) - length + 1):
        # Extract the substring of the same length as 'char' starting from the current position
        if main_string[i:i+length] == char:
            occurrences += 1  # Increment the counter if a match is found
    
    return occurrences  # Return the total number of occurrences
    
      

def find_all_substrings(main_string, char):
    """
    Function to find all substrings starting with a certain character in a given string.

    Args:
    main_string (str): The main string in which occurrences will be found.
    char (str): The character to check for at the beginning of substrings.

    Returns:
    list: A list containing the substrings starting with the specified character.
    """
    substrings = []  # Initialize an empty list to store the substrings
    
    for i in range(len(main_string)):
        # Check if the current character matches the specified character
        if main_string[i] == char:
            # Append the substring starting from the current position to the end of the list
            substrings.append(main_string[i:])
    
    return substrings  # Return the list of substrings

def main():
    """
    Main function to accept input and print out results.
    """
    main_string = input("Enter the main string:\n")
    starting_char = input("Enter the character to search for at the beginning of substrings:\n")
    starting_char = starting_char.lower()
    main_string = main_string.lower()

    count = count_substrings(main_string, starting_char)
    print("Number of substrings starting with '{}': {}".format(starting_char, count))

    substrings = find_all_substrings(main_string, starting_char)
    if substrings:
        print("Substrings starting with '{}':".format(starting_char))
        print(", ".join(substrings))
        #for substring in substrings:
        #    print(substring)
    else:
        print("No substrings starting with '{}' found.".format(starting_char))

if __name__ == "__main__":
    main()