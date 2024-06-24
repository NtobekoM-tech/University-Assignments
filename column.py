#Program to print out every 7th number in the range n to n+41.
#Ntobeko Mhlongo
#11 March 2024

# Prompt the user to enter a number between -6 and 2
user_input = input("Enter a number between -6 and 2:\n")

n = int(user_input)

# Check if the input number is within the specified range
if -6 < n < 2:
    # Loop to print every 7th number in the range from n to n + 41
    for i in range(n, n + 42, 7):
        print(f' {i:2}')  # Print the number with a minimum width of 2 characters
        
else:
    # Print an error message for invalid input
    print("Invalid input! The value of 'n' should be between -6 and 2.")