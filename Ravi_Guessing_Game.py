import random

high_score = 1000

def outline(message):
    print("-" * len(message))
    print(message)
    print("-" * len(message))


def number_guessing_game():
    global high_score #Learned from https://www.geeksforgeeks.org/global-local-variables-python/
    global keep_playing
    number = random.randint(1, 10)
    number_of_guesses = 0
    while True:     #continuosly prompts for guess and tells if it is higher or lower
        player_guess = input("Pick a number between 1 and 10: ")
        try:
            player_guess = int(player_guess)
            if player_guess < 1 or player_guess > 10: #Makes sure guess is between 1 and 10
                raise ValueError("{} is not between 1 and 10".format(player_guess))
        except ValueError as err:
            if ("invalid literal" in str(err)): #Throws error if a number was not inputed
                print("Sorry, {} is not a valid input".format(player_guess))
                continue
            else:
                print("Sorry there was an issue. {}. Please try again.".format(err))
                continue
        
        if player_guess == number:
            number_of_guesses += 1
            print()
            outline("{} was my number! It took you {} guesses!".format(number, number_of_guesses))
            break
        elif player_guess < number:
            print("{} is lower than my number".format(player_guess))
            number_of_guesses += 1
            continue
        elif player_guess > number:
            print("{} is higher than my number".format(player_guess))
            number_of_guesses += 1
            continue
    if number_of_guesses < high_score:
        high_score = number_of_guesses
    print()

    while True:
        keep_playing = input("Would you like to play again? (Y/N) ")
        print()

        try:    #makes sure "y" or "n" was entered
            keep_playing = keep_playing.lower()
            if keep_playing == "n":
                outline("Have a great day!")
                break
            elif keep_playing != "y":
                raise ValueError
        except ValueError:
            print("You must enter 'Y' or 'N'. Please try again.")
            continue
        if keep_playing.lower() == "y":     #plays game again or quits the game based on user input
            outline("The score to beat is {}!".format(high_score))
            number_guessing_game()


outline("Welcome to Ravi's Number Guessing Game")
number_guessing_game()










