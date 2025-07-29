print("welcome to order pizza")
size = input(" what size do you want: small, medium or large : ")
pep = input ('do you want pepperoni? y or n : ')
cheese = input ("do you want extra cheese? y or n : ")
bill = 0
if size == "small":
    bill += 15
    if pep == "y":
        bill += 2
elif size == 'medium':
    bill += 20
    if pep == "y":
        bill += 3
elif size == 'large':
    bill += 25
    if pep == "y":
         bill += 3
if cheese == "y":
        bill += 1
print(f"total bill is ${bill}.")




