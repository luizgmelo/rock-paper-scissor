# Rock Paper Scissors
import random

while True:    
    alternatives = ["rock", "paper", "scissors"]
    player = str(input("Rock, Paper or Scissors: ")).lower()
    computer = random.choice(alternatives)
    
    if player not in alternatives:
        print("Invalid Option")
        continue
    
    print(f"You are {player} and computer is {computer}") 
    
    if (player == computer):
        print("Draw!")
    # Rock win scissorss
    elif (player == "rock" and computer == "scissors"):
        print("Win!")
    # Paper win Rock
    elif (player == "paper" and computer == "rock"):
        print("Win!")
    # scissorss win Paper
    elif (player == "scissors" and computer == "paper"):
        print("Win!")
    else:
        print("Lose!")
    
    break
    # Equal is draw
