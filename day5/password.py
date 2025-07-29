import random
# letters = ['a','b','c','d','e','f','g','h','i','j','k','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# number = ['1','2','3','4','5','6','7','8','9',]
# symbol = ['#','$','&','(',')','*','+']
# print("welcome to the password generator!")
# lett = int(input("how many letters would you like in your password?\n"))
# sym = int(input("how many symbols would you like?\n"))
# num = int(input("how many numbers would you like?\n"))
# password = ""
# for char in range(1,lett + 1 ):
#     password += random.choice(letters)
# for num in range(1,num + 1):
#     password += random.choice(number)
# for sym in range(1,sym + 1):
#     password += random.choice

# print(password)
letters = ['a','b','c','d','e','f','g','h','i','j','k','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9',]
symbol = ['#','$','&','(',')','*','+']
print("welcome to the password generator!")
lett = int(input("how many letters would you like in your password?\n"))
sym = int(input("how many symbols would you like?\n"))
num = int(input("how many numbers would you like?\n"))
password_list = []
for char in range(1,lett + 1 ):
     password_list += random.choice(letters)
for num in range(1,num + 1):
     password_list += random.choice(number)
for sym in range(1,sym + 1):
     password_list += random.choice(symbol)
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
     password += char
print(f"your password is: {password}")
