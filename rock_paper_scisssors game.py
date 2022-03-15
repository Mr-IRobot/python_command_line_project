import random
from ssl import Options

user_wins = 0
computer_wins = 0

Options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose between rock, paper and scissors to play Or Q to quit | ").lower()
    if user_input == "q":
        break
    if user_input not in Options:
        print("Pls enter a valid answer")
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2

    computer_pick = Options[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print("Congratulations! You won")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Congratulations! You won")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("Congratulations! You won")
        user_wins += 1
    elif user_input == computer_pick:
        print("Equalized! Nobody won")
        user_wins += 0
    else:
        print("You lost")
        print("Computer won")
        computer_wins += 1

print ("You won", user_wins, "times")
print ("computer won", computer_wins, "times")
print ("Goodbye!")