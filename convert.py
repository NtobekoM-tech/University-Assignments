# Program to convert  a date and time given in a compact 24-hour format to a long form 12-hour format
# Ntobeko Mhlongo
# 20 March 2024

date_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

# Slicing the year,month,day,hour and minute from the yyyy-mm-dd hh:mm format
year = date_time[:4]
month = date_time[5:7]
day = date_time[8:10]
hour = date_time[11:13]
minute = date_time[14:16]

# Converting the hours to the 12 hour formart
hour_int = int(hour) # Converting the input hour to integer for comparison
if hour_int < 12: # If the hour is less than 12, the time suffix will be 'am' 
    period = 'am'
    if hour_int == 0: # If the hour is equal to 0, then the new format hour will be 12
        hour_int = 12
else: # If the hour is greater than 12, the time suffix will be 'pm'
    period = 'pm'
    if hour_int != 12:
        hour_int -= 12 # Subtract 12 from hour to get pm format
hour = str(hour_int) # Convering hour bact to the string format



# Adding sifffixes on the days
day_int = int(day)# Converting the day to an integer for comparisson
if day_int % 10 == 1 and day_int != 11:# If the day ends with 1 and its not 11, then the suffix is 'st'
    day_suffix = 'st'
elif day_int % 10 == 2 and day_int != 12:# If the day ends with 2 and its not 12, then the suffix is 'st'
    day_suffix = 'nd'
elif day_int % 10 == 3 and day_int != 13:# If the day ends with 3 and its not 13, then the suffix is 'st'
    day_suffix = 'rd'
else: # If none of the above conditions are true, then the safix is 'th'
    day_suffix = 'th'
day = str(day_int)# Converting the day back to a string

# Matching the number month given on the input to the name of the month corresponding to that number
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']# Month names in their order
month_name = months[int(month) - 1] # This gives back the name of the month corresponding to the number from input

print(hour + ':' + minute,  period + ' on the ' + day + day_suffix + ' of ' + month_name + ' \'' + year[2:])