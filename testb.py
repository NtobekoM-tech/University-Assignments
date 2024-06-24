#Program to count and sum up the number of adjecent pairs of multiples of 4
#Ntobeko Mlongo
#2024-04-02

count = 0  # Initialize count for multiples of 4
stop = 'DONE'  # Define the stopping condition
number = input("Enter a number (or 'DONE' to end):\n")  # Prompt user for input

while number != stop:
    # Check if input is a valid number
    if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
        value = int(number)  # Convert input to integer
        
        if value % 4 == 0:  # Check if the number is a multiple of 4
            count += 1  # Increment count if it is a multiple of 4

    number = input("Enter a number (or 'DONE' to end):\n")  # Prompt user for next input

total = count * 4  # Calculate total sum of multiples of 4

# Print the results
print("Number of multiples of 4:", count, end=". ")
print("Sum of multiples of 4:", total, end=".")