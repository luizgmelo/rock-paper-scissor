# Rock Paper Scissors
import random

while True:    
    alternatives = ["rock", "paper", "scissor"]
    player = str(input("Rock, Paper or Scissor: ")).lower()
    computer = random.choice(alternatives)
    
    if player not in alternatives:
        print("Invalid Option")
        continue
    
    print(f"You are {player} and computer is {computer}") 
    
    if (player == computer):
        print("Draw!")
    # Rock win Scissors
    elif (player == "rock" and computer == "scissor"):
        print("Win!")
    # Paper win Rock
    elif (player == "paper" and computer == "rock"):
        print("Win!")
    # Scissors win Paper
    elif (player == "scissor" and computer == "paper"):
        print("Win!")
    else:
        print("Lose!")
    
    break
    # Equal is draw
