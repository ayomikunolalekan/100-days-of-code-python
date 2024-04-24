print("GUESS THE NUMBER ✨✨")
print()
print("Instructions: A number between 1 and 1000000 has been chosen as the mystery number, your task is to guess the exact number. Have fun playing 😁😁")
mysteryNumber = 50000
numberOfAttempts = 1


while True:
  print()
  userGuess = int(input("Guess my mystery number: "))
  if userGuess > mysteryNumber:
    print("Your guess is too high 😬😬")
  elif userGuess < mysteryNumber and userGuess > 0:
    print("Your guess is too low 😔😔")
  elif userGuess <= 0:
    print("BYE BYE 👋")
    exit()
  else:
    print("You have guessed correctly 🥳🥳")
    break

  numberOfAttempts += 1

print()
print("It took you", numberOfAttempts, "attempt(s) to correctly guess the number.")
