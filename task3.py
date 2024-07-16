import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):  ").lower()
    options = ["rock", "paper", "scissors"]
    if player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return get_choices()
    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}

def check_win(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return f"{player.capitalize()} beats {computer}! You win!"
    else:
        return f"{computer.capitalize()} beats {player}! You lose."

def play_game():
    while True:
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)

        con = input("Do you want to continue (Y for yes/N for no)?: ").strip().upper()
        if con == 'N':
            print("THANK YOU!")
            break
        elif con != 'Y':
            print("Invalid input, exiting the game.")
            break

if __name__ == "__main__":
    play_game()

exit()
import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):  ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock Smashes Scissors! You Win!"
        else:
            return "Paper Covers Rock! You Lose."
    elif player == "paper":
        if computer == "rock":
            return "Rock Smashes Scissors! You Win!"
        else:
            return "Scissors cuts Paper! You Lose."
    elif player == "Scissor":
        if computer == "rock":
            return "Rock Smashes Scissors! You lose!"
        else:
            return "Scissors cuts Paper! You Win."

def game():
    while True:
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)
def cont():
    con = str(input("Do you want to Continue(Y for yes/N for no)?:"))
    if con == "Y":
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)
    elif con == "N":
        print("THANK YOU !")
        exit()
    else:
        cont()

game()
cont()

