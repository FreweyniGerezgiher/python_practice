import random
word_list = ['dad','good','better']
choosen_word = random.choice(word_list)
display = []
for letter in choosen_word:
    display += "_"
print(display)
#x = len(choosen_word)
# while x > 0:
#     x -= 1
#     display += "_"
end_game = False
lives = 6
#from hangman_art import log

while not end_game:
    guess = input("guess a letter:").lower()
    # if guess in display:
    #     print(f"you've already guessed{guess}")
    for pos in range(len(choosen_word)):
        letter = choosen_word[pos]
        if letter == guess:
            display[pos] = letter 
    print(display)
    if guess not in choosen_word:
        print(f"you guessed {guess}, that's not in the word. you lose a life.")
        lives -= 1
        if lives == 0:
            end_game = True    
            print("Game over!")
    
    if "_" not in display:
        end_game = True
        print("you win.")
    # from hangman_art import stages
    # print(stages[lives])   


