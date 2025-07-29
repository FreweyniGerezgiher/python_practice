import random
game_images = ['rock', 'paper', 'scissors']
choosen = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors."))
comp = random.randint(0,2)
if choosen >= 3 or choosen < 0:
    print("you typed an invalid number, you lose!")
else:
    print("you choose :")
    print(game_images[choosen])
    print("computer choose:")
    print(game_images[comp])

    if choosen == '0' and comp == '2':
        print(" You Win!")
    elif comp == 0 and choosen == 2:
        print("You lose!")
    elif comp > choosen:
        print("you lose!")
    elif choosen > comp :
        print("You win!")
    elif comp == choosen:
        print(" It is a draw!")