print("wellcome to know your body mass")
weight = float(input("enter your weight:\n"))
height = float(input("enter your height:\n"))
body_mass = int(weight/(height**2))

if body_mass <= 18.5:
    print(f"your body mass is {body_mass} you are underweight")
elif body_mass < 25:
    print(f"your body mass is {body_mass} you have a normal weight")
elif body_mass < 35:
    print(f"your body mass is {body_mass} you are overweight")
else:
    print(f"your body_mass is{body_mass}, you are critically obese ")        