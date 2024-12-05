from random import *

# computer chooses a random number between 1 and 6
ranumb = randint(1,6)
#user inputs a number between 1 and 6
usernumb = int(input("Enter a number between 1 and 6: "))
#if the user's number is the same as the computer's number, the user wins
if usernumb == ranumb:
  print("You win!") 
#if the user's number is not the same as the computer's number, the user loses
else:
  print("you lose")