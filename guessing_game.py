## A simple 'guess the number' game! ##

import random
import pdb

guesses = 0

solved = False


def start_game():
    global solved
    global answer
    global guesses

    solved = False
    answer = random.randrange(1,10)
    guesses = 0
    game_on()


def game_on():
    global solved
    global guesses
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
            game_winner()


def game_winner():
    print(f"You won the game!! It took you {guesses} guesses.")
    play_again = None
    while play_again.lower() not in ("y", "n"):
        try:
            play_again = input("Would you like to play again? Y/N \n")
            if play_again.lower() != "y" or play_again.lower() != "n":
                print("Sorry, I didn't understand.  Please press Y for yes and N for no.")
            if play_again.lower() == "y":
                start_game()
            else:
                print("Thank you for playing!")
# start_game()