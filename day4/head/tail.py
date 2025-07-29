import random
#random_side = random.randint(0,1)
#if random_side == 1:
 #   print("heads")
#else:
 #   print("tails")
name = input("give me every body\'s names, separeted by a comma. ")
name = name.split(",")
print(name)
x = len(name)
choosen = random.randint(0,x - 1)
person = name[choosen]
print(person + "  will pay the bill")
    