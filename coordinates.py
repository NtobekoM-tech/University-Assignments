#Program to check if a set of 6 numbers is a pair of GPS coordinates or not
#Ntobeko Mhlongo
#06-03-2024

latitude_degrees = int(input("Enter latitude degrees:\n"))
latitude_minutes = int(input("Enter latitude minutes:\n"))
latitude_seconds = int(input("Enter latitude seconds:\n"))
longitude_degrees = int(input("Enter longitude degrees:\n"))
longitude_minutes = int(input("Enter longitude minutes:\n"))
longitude_seconds = int(input("Enter longitude seconds:\n"))

# Validate latitude and longitude values
if (-90 <= latitude_degrees <= 90 and 0 <= latitude_minutes <= 59 and 0 <= latitude_seconds <= 59 and
        -180 <= longitude_degrees <= 180 and 0 <= longitude_minutes <= 59 and 0 <= longitude_seconds <= 59):
    print("WOW! Looks like geographic coordinates!")
else:
    print("Hmmm ... looks like 6 random numbers.")
