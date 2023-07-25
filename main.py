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
    print(showArt(player), end="")
    print(showArt(computer, True))

    if (player == computer):
        print("Draw!".center(20))
    # Rock win scissorss
    elif (player == "rock" and computer == "scissors"):
        print("Win!".center(20))
    # Paper win Rock
    elif (player == "paper" and computer == "rock"):
        print("Win!".center(20))
    # scissorss win Paper
    elif (player == "scissors" and computer == "paper"):
        print("Win!".center(20))
    else:
        print("Lose!".center(20))
    
    break
    # Equal is draw

