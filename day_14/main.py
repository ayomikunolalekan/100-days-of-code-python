from getpass import getpass as input
print("ROCK PAPER SCISSORS 🪨📃✂️")
print()
print("Instructions: This game is a two player game where each player gets the chance to pick either rock, paper or scissors. When drawing or picking, we advise you make use of R to represent rock, P to represent paper and S to represent scissors. Have fun 😁😁")
print()

player1Pick = input("What do you pick player 1?: ")
player2Pick = input("Player 2, what do you pick?: ")
print()

if player1Pick == "R" or player1Pick == "r":
  if player2Pick == "R" or player2Pick == "r":
    print("Player 1 picks rock and so does player 2, we have a draw!!")
  elif player2Pick == "P" or player2Pick == "p":
    print("Omg 😱😱, player 2 paper completely smothers player 1 rock.")
  elif player2Pick == "S" or player2Pick == "s":
    print("Smash 💥💥, player 1 rock completely smashes player 2 scissors.")
  else:
    print("Sorry but you can't pick that, please check the instructions again. 🙇‍♂️")

elif player1Pick == "P" or player1Pick == "p":
  if player2Pick == "R" or player2Pick == "r":
    print("Super smother 😂😂, player 1 paper smothers player 2 rock into oblivion")
  elif player2Pick == "P" or player2Pick == "p":
    print("Paper and Paper, subarashi, we have a draw 😰😰")
  elif player2Pick == "S" or player2Pick == "s":
    print("Cut Cut Cut ✂️✂️, the power of player 2 scissors has been revealed as it mercilessly cuts player 1 paper to shreds.")
  else:
    print("Sorry but you can't pick that, please check the instructions again. 🙇‍♂️")

elif player1Pick == "S" or player1Pick == "s":
  if player2Pick == "R" or player2Pick == "r":
    print("Smash fest 🔥🔥, player 1 scissors gets completely annihilated by player 2 rock.")
  elif player2Pick == "P" or player2Pick == "p":
    print("What in the world am I seeing 🫢🫢, player 1 scissors is cutting player 2 paper beyond imagination.")
  elif player2Pick == "S" or player2Pick == "s":
    print("Oh mighty scissors, you have clashed and as you have clashed, there can be no winner, we have a draw.")
  else:
    print("Sorry but you can't pick that, please check the instructions again. 🙇‍♂️")

else:
  print("Please check the instructions again, you can't pick an option that is not suggested.")