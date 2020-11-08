## A simple 'guess the number' game! ##

import random

## maybe add extra functionality? Like displaying what the old scores were, or how many times the game has been played ##
scores = [100000,]

def game_on():
    solved = False
    answer = random.randrange(1,11)
    guesses = 1
    while solved == False:
        try:
            guess = int(input("Guess a number between 1 and 10.\n"))
            if guess > 10 or guess < 1:
                raise 
        except:
            print("That's not a valid option!\n")
            continue
        if guess > answer:
            print("Your guess was too high!")
            guesses += 1
        elif guess < answer:
            print("Your guess was too low!")
            guesses += 1
        elif guess == answer:
            solved = True
            game_winner(guesses)


def game_winner(guesses):

    high_score = min(scores)
    play_count = len(scores)
    if high_score > guesses:
        print(f"You won game {play_count} AND beat the old high score!!  New high score is {guesses} guesses.")
    elif high_score == guesses:
        print(f"You won game {play_count} AND tied the high score!! High score is {guesses} guesses.")
    else:
        print(f"You won game {play_count}!! It took you {guesses} guesses.  The current high score is {high_score} guesses.")
    
    play_again = ""
    scores.append(guesses)

    while play_again.lower() not in ("y", "n"):
            play_again = input("Would you like to play again? Y/N \n")
            if play_again.lower() == "y":
                game_on()
            elif play_again.lower() == "n":
                print("Thank you for playing!")


game_on()