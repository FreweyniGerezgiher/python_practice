import random
data = [
    {
     'name': 'instagram',
     'follower': 346,
     'description': 'social media platform',
     'country': 'united states'

    } ,
    {
     'name': 'cristiano ronaldo',
     'follower': 215,
     'description': 'footballer',
     'country': 'portugal'


    },
    {
     'name': 'ariana',
     'follower': 183,
     'description': 'musician',
     'country': 'united states'

    },
    {
     'name': 'dwayne johnsen',
     'follower': 181,
     'description': 'actor and professional wrestler',
     'country': 'united states'

    },
    {
     'name': 'selina gomez',
     'follower': 174,
     'description': 'musician and actress',
     'country': 'united states'

    },
    {
     'name': 'kylie jenner',
     'follower': 172,
     'description': 'business woman and self-made billionere',
     'country': 'united states'

    },
    {
     'name': 'kim kardashian',
     'follower': 167,
     'description': 'reality tv personality and businesswoman ',
     'country': 'united states'

    },
    {
     'name': 'lionel messi',
     'follower': 149,
     'description': 'footballer',
     'country': 'arjentina'

    }
]
def compare(a, b):
    if a['follower'] > b['follower']:
        return 'a'
    elif a['follower'] < b['follower']:
        return 'b'
    else:
        return "its a tie"
ans = "correct"        
game_over = False
while not game_over:
    def game():
        global ans
        first = {} 
        first = random.choice(data)
        second = {}
        second = random.choice(data)
        print(f" compare A: { first['name']},{first['description']}, from {first['country']} ")
        print("versus")
        print(f"against B:{ second['name']},{second['description']}, from {second['country']}  ")
        
        answer = input("who has more followers? 'a' or 'b': ")
        if answer == compare(first, second):
            print("correct")
            # return 'correct'
            ans = "correct"
        else:
            print("incorrect")
            ans = "incorrect"
            # return 'incorrect'

        # print(compare(first, second))
        
                    
    
        if ans == 'incorrect':
            print("game over")
            play_again = input("play again? 'y' or 'n': ")
            if play_again == 'y':
                game()
            else:
             game_over = True

            # game_over = True  
            
            # if play_again == 'n' :
            #     game_over = True
            #     print("game over")
            # else:
            #     game()
        else:
            game()
    game()

             


