from random import randint
from colorama import Fore, Back, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_score = 0
computer_score = 0
draws = 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: \n")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"\nThe computer chose {computer_move}.\n")

    # Scoreboard
    if player_move == computer_move:
        draws += 1
        print(Fore.YELLOW + "Draw!")
        print(Style.RESET_ALL)
        print("Player:" + str(player_score) + ' | ' + "Computer:" + str(computer_score) + ' | ' + "Draws:" + str(
            draws))

    if player_move == "Rock" and computer_move == "Scissors":
        player_score += 1
        print(Fore.BLUE + "You win!")
        print(Style.RESET_ALL)
        print("Player:" + str(player_score) + ' | ' + "Computer:" + str(computer_score) + ' | ' + "Draws:" + str(
            draws))

    if player_move == "Rock" and computer_move == "Paper":
        computer_score += 1
        print(Fore.RED + "You lose!")
        print(Style.RESET_ALL)
        print("Player: " + str(player_score) + ' | ' + "Computer: " + str(computer_score) + ' | ' + "Draws: " + str(
            draws))

    if player_move == "Paper" and computer_move == "Rock":
        player_score += 1
        print(Fore.BLUE + "You win!")
        print(Style.RESET_ALL)
        print("Player: " + str(player_score) + ' | ' + "Computer: " + str(computer_score) + ' | ' + "Draws: " + str(
            draws))

    if player_move == "Paper" and computer_move == "Scissors":
        computer_score += 1
        print(Fore.RED + "You lose!")
        print(Style.RESET_ALL)
        print("Player: " + str(player_score) + ' | ' + "Computer: " + str(computer_score) + ' | ' + "Draws: " + str(
            draws))

    if player_move == "Scissors" and computer_move == "Paper":
        player_score += 1
        print(Fore.BLUE + "You win!")
        print(Style.RESET_ALL)
        print("Player: " + str(player_score) + ' | ' + "Computer: " + str(computer_score) + ' | ' + "Draws: " + str(
            draws))

    if player_move == "Scissors" and computer_move == "Rock":
        computer_score += 1
        print(Fore.RED + "You lose!")
        print(Style.RESET_ALL)
        print("Player: " + str(player_score) + ' | ' + "Computer: " + str(computer_score) + ' | ' + "Draws: " + str(
            draws))
    print()
    play_again = input("Would you like to play again? (y/n)")
    print()
    if play_again.lower() != "y":
        print("Thank you for playing!")
        break
