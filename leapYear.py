# Program to determine if the given year is a leap year or not.
# Ntobeko Mhlongo

year = int(input("Enter a year:\n"))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
      string_in_string = "{} is a leap year.".format(year)
      print(string_in_string)
else:
      string_in_string = "{} is not a leap year.".format(year)
      print(string_in_string)
      