# Program to create a spam letter using details provided by the user 
# Ntobeko Mhlongo

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = int(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

money30 = money * 0.3

print("\nDearest", first_name)
print("It is with a heavy heart that I inform you of the death of my father,")
print(f"General Fayk {last_name}, your long lost relative from Mapsfostol.")
print(f"My father left the sum of {money} USD for us, your distant cousins.")
print(f"Unfortunately, we cannot access the money as it is in a bank in {country}.")
print("I desperately need your assistance to access this money.")
print(f"I will even pay you generously, 30% of the amount - {money30} USD, for your help.")
print("Please get in touch with me at this email address asap.")
print("Yours sincerely,")
print(f"Frank {last_name}")
