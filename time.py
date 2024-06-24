# Program to determine if the time provided by the user is valid or not 
# Ntobeko Mhlongo
hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))
if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
