"""
Program to determine and prints out if a given number is a perfect number or not. It also prints out the divisors of the given number 
Ntobeko Mhlongo
05-03-2024
"""

number = int(input("Enter a number:\n"))

result = 0 #initial value of the result
print("The proper divisors of",number,"are:")
#finding divisors and adding them to the result
for i in range(1,number):
    if number % i == 0:
        result += i
        print(i, end=' ')

if result == number:
    print()
    print()
    print(number, "is a perfect number.")
    
else:
    print()
    print()
    print(number, "is not a perfect number.")