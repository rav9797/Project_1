import random


def welcome():
    welcome_message = "Welcome to Ravi's Number Guessing Game!"
    print("-" * len(welcome_message))
    print(welcome_message)
    print("-" * len(welcome_message))


def start_game():
    number = random.randint(1, 10)
    number_of_guesses = 0
    while True:
        player_guess = input("Pick a number between 1 and 10: ")
        player_guess = int(player_guess)

        if player_guess == number:
            number_of_guesses += 1
            print("{} was my number! It took you {} guesses!".format(number, number_of_guesses))
            break
        elif player_guess < number:
            print("{} is lower than my number".format(player_guess))
            number_of_guesses += 1
            continue
        elif player_guess > number:
            print("{} is higher than my number".format(player_guess))
            number_of_guesses += 1
            continue
    keep_playing = input("


welcome()
start_game()








