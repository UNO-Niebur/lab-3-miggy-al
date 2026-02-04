#RPS.py
#Name: Miguel Alvarado
#Date: 2/2/2026
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  playagain = "Y"
  #Create a loop that continues as long as the user wants to play.
  while playagain == "Y":
    #User can play as many games as they wish.
    computer = random.choice( ["R", "P", "S"])
    player = input("Choose wisley (R, P, S):")
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose R")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")

    if player == computer:
     print("It's a tie!")
     ties = ties + 1
    elif ((player == "R" and computer == "S") or 
     (player == "P" and computer == "R") or 
     (player == "S" and computer =="P")):
     print("You win!")
     wins = wins + 1
    else:
      print("You lose!")
      losses = losses + 1
   #Ask the user if they would like to play again.
    playagain = input("Do you want to play again? (Y/N):")
  
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
