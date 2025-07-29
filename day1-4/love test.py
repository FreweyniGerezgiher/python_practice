print("welcome to love test!")
name1 = input("enter the first name: ")
name2 = input("enter the second name: ")
combn = name1 + name2
combn = combn.lower()

t = combn.count('t')
r = combn.count('r')
u = combn.count('u')
e = combn.count('e')
true = t + r + u + e
l = combn.count('l')
o = combn.count('o')
v = combn.count('v')
e = combn.count('e')
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) and (love_score > 90):
    print(f"your love score is {love_score}% ,you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f" your score is {love_score}, you are alright together.")
else:
    print(f"your love score is {love_score}%.") 