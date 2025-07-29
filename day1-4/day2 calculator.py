print("wecome to the tip calculator.")
bill = int(input("what was the total bill?\n"))
percent = int(input("what percentage tip would you like to give?\n"))
people = int (input("how many people to split the bill?\n"))
percentage = bill*percent/100
payment = round((bill + percentage)/people,)
print(f" Each person should pay : ${payment}")