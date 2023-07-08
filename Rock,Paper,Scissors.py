import random
print(" Hello welcome to this fun python game! by yumbiakyumu. It is rock,paper,scissors intreactive game built using python. The game has three tries per round and at the end of one round the winner is determined. ENJOY!!\n")
def get_choices():
    players_choice = input("Enter a choice (rock, paper, or scissors): ")
    options = ["rock", "paper", "scissors"]
    while players_choice not in options:
        print("Invalid choice! Please try again.")
        players_choice = input("Enter a choice (rock, paper, or scissors): ")

    computers_choice = random.choice(options)
    choices = {"player": players_choice, "computer": computers_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock": 
        if computer == "scissors":
            return "Rock smashes the scissors!! YOU WIN!"
        else: 
            return "Paper covers the rock!! Computer WINS LOL!!"
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers the rock!! You WIN hurray!!"
        else: 
            return "Scissors snips paper!! Computer takes this one you lose!"
    elif player == "scissors": 
        if computer == "paper":
            return "Scissors cuts paper!! Lucky one you WIN!!"
        else: 
            return "Rock destroys scissors!! HAHA you lose!"

player_wins = 0
computer_wins = 0
rounds = 3
current_round = 1

while current_round <= rounds:
    print(f"Round {current_round}")
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    print()  # Add a blank line for spacing

    if "YOU WIN" in result:
        player_wins += 1
    elif "Computer WINS" in result:
        computer_wins += 1

    current_round += 1

    if current_round <= rounds:
        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            break

print()  # Add a blank line for spacing

if player_wins > computer_wins:
    print("Congratulations! You won the round!")
elif player_wins < computer_wins:
    print("Sorry, the computer won the round!")
else:
    print("It's a tie! No winner for this round.")
    
