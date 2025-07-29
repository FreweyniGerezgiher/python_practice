from random import randint
easy_turns = 10
hard_turns = 5

def game():
    def compare(num,guess,turns):
        if guess == num:
            print(f"you got it! the answer was {num}")
            game_over = True
        elif guess < num:
            print("too high!")
            return turns - 1
        else:
            print("too low!")
            return turns - 1
            
    def set_difficulty():
        level = input("choose a difficulty. type 'easy'or 'hard': ")
        if level == "easy":
            return easy_turns
        else:
            return hard_turns
    print("welcome to number guessing game!")
    print("i am thinking of a number between 1 and 100.")
    # game_over = False
    num = randint(1,100)
    print(num)

    turns = set_difficulty()
    guess = 0
    while guess != num:
        print(f"you have {turns} attempts remaining.")

        guess = int(input("guess the random number:"))
        turns = compare(guess, num, turns)
        if turns == 0:
            print("you have run out of guess, you lose")
            return
        elif guess != num:
            print("guess again")
        
game()


# def easy():
#     for _ in range(10):
#         compare()
#         # easy()
# def hard():
#     for _ in range(5):
#         compare()
#         # hard()
# while not game_over:
#     if choose == "easy":
#         easy()
#     if choose == "hard":
#         hard()
            