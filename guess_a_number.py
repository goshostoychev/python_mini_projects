# Python guess a number game

# Import additional libraries
from random import randint
from colorama import Fore, Style, init

# This is used to reset the styling after each printed message
init(autoreset=True)
loop = True
# Game logic
while loop:
    print(Fore.GREEN + "Welcome to Guess the number game!\n")
    difficulty = input(Fore.YELLOW + "Choose a difficulty level - Easy, Medium, or Hard: \n").lower()
    computer_number = randint(1, 1)

    if difficulty == "easy":
        computer_number = randint(1, 100)
    elif difficulty == "medium":
        computer_number = randint(1, 200)
    elif difficulty == "hard":
        computer_number = randint(1, 300)
    else:
        print(Fore.RED + "\nInvalid difficulty level. Playing on Easy.\n")

    max_attempts = int(input("Choose number of attempts:\n"))

    attempts = 0

    while attempts < max_attempts:

        player_input = input(Fore.LIGHTGREEN_EX + f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: \n")

        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Try again...")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            print(Fore.GREEN + f"\nYou guessed the number '{computer_number}' correctly after {attempts + 1} attempts.")
            break
        elif player_number > computer_number:
            print(Fore.YELLOW + "Your number is too high!\n")
        elif player_number < computer_number:
            print(Fore.MAGENTA + "Your number is too low!\n")

        attempts += 1

    if attempts == max_attempts:
        print(Fore.RED + f"Sorry, you've run out of attempts. The computer's number was {computer_number}.")
    play_again = input(Fore.BLUE + "\nWould you like to play again? (y/n)\n").lower()
    if play_again == "y":
        continue
    elif play_again != "y":
        loop = False
        print("Thank you for playing!")
    break