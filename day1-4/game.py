print("welcome to treasure island. your mission is to find the treasure.")
direction = input(" you are at the cross road.which direction do you want to go? left or right :  ")
if direction == 'left':
    choose = input("do you want to swim or wait? ")
    if choose == 'wait':
        door = input("which door? red, blue or yellow? ")
        if door == 'yellow':
            print("you found the treasure. you Win!")
        else:
            print("game over")    
    else:
        print("you got attacked. game over")
else:
    print("you fell in to a hole. game over")        