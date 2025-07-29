print("wellcome to know how many years you have left to die")
age = int(input("enter your age:\n"))
days = (90-age)*365
weeks = (90-age)*12*7
months = (90-age)*12
years = (90-age)
print(f"you have left with {days}days, {weeks} weeks, {months} months and {years} years.")