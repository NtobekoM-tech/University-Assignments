#Program to calculate the volume and the postage cost of a parcel
#Ntobeko Mhlongo
#05-03-2024

l = eval(input("Enter the length:\n"))
w = eval(input("Enter the width:\n"))
h = eval(input("Enter the height:\n"))

Volume = l*h*w # Formula to calculate the volume
if (Volume <= 0):
    print("Dimensions must be greater than zero.")
elif (0 < Volume < 18):
    print("The volume is %.2f" %Volume , end='.\n')
    print("Shipping cost is 14.65.")
elif (18 <= Volume < 140):
    print("The volume is %.2f" %Volume , end='.\n')
    print("Shipping cost is 5.95.")
elif (140 <= Volume < 440):
    print("The volume is %.2f" %Volume , end='.\n')
    print("Shipping cost is 12.00.")
elif (440 <= Volume < 2648):
    print("The volume is %.2f" %Volume , end='.\n')
    print("Shipping cost is 14.65.")    
else: 
    print("The volume is %.2f" %Volume , end='.\n')
    print("Shipping cost is not available.")
    print("Package too large.")
