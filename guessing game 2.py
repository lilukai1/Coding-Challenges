## A simple 'guess the number' game! ##

import random

def game_on():
    solved = False
    answer = random.randrange(1,10)
    guesses = 1
    while solved == False:
        try:
            guess = int(input("Guess a number between 1 and 10.\n"))
        except:
            print("That's not a valid option!\n")

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
    print(f"You won the game!! It took you {guesses} guesses.")
    play_again = ""
    while play_again.lower() not in ("y", "n"):
            play_again = input("Would you like to play again? Y/N \n")
            if play_again.lower() == "y":
                game_on()
            elif play_again.lower() == "n":
                print("Thank you for playing!")


game_on()