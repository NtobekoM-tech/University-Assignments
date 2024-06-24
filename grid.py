#Program to print out numbers n to n+41 as 6 rows of 7 numbers.
#Ntobeko Mhlongo
#12 March 2024

n = eval(input("Enter a number between -6 and 2:\n"))

if -6 < n < 2:#Checks of the value provided by user is within the range.
    for i in range(n, n + 42, 7):# Loop to print every 7th number in the range n to n + 41.
        for j in range(i, i + 7):# Loop to print out the number of colums
            print(f'{j:2}', end = ' ') 
        print()  # Print a newline after each row
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")