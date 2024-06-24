"""
Program to reformat references using the assumption that the input reference format is:
a list of authors, space, (year), space, title, comma, other information.
Ntobeko MHlongo
20 March 2024
"""

reference = input("Enter the reference:\n")

# Slicing out the year from the input
year_start = reference.find("(")
year_end = reference.find(")")
year = reference[year_start + 1 : year_end]#adds 1 on year_start because the year beggins after the bracket

authors = reference[:year_start].title()#slicing out the authors from the input and capitalizing the first letter of each word

#slicing out the title from the input
title_start = year_end + 2
title_end = reference.find(",", title_start)#title ends at the first comma after the title beggins
title = reference[title_start : title_end]
title = title[0].title() + title[1:].lower()#capitalizing only the first letter of the title and making the rest of the title lower cases

other_information = reference[title_end + 1 :]#slicing out the remaining information until the end of the reference

print("Reformatted reference:")
print(authors + "("+year+")", title+"," + other_information)