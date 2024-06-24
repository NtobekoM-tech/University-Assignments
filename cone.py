#Program to calculate and print volume rounded up to 2 decimal places using given values
#Ntobeko Mhlongo

from math import pi

h = input("Enter the height of the cone:\n")
r = input("Enter the radius of the base:\n")
height = eval(h)
radius = eval(r)
volume = height/3*pi*radius**2
rounded_volume = round(volume, 2)
if height > 0 and radius > 0:
    print("The volume is", rounded_volume)
else:
    print("The height and radius must be greater than zero.")