# Rock Paper Scissors
import random

def showArt(alternative, computer=False):
    if computer == True:
        if alternative == "rock":
            return """
    _______
   (____)  '---
  (____)
  (_____)
  (____)
  (___)__.---

"""
        elif alternative == "paper":
            return """
       ______
   ___(__    '---   
  (_____
  (_______
   (_______
    (__________.---

"""
        elif alternative == "scissors":
            return """
        _______
    ___(____   '---
   (______
  (_______
     (____)
      (___)__.---
 
 """
    else:

        if alternative == "rock":
            return """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)"""
        elif alternative == "paper":
            return """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    
        """
        else:
            return """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """
    

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
