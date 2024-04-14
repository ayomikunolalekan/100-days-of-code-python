print("ANIMAL SOUNDS 🫏🫏")
print()
userExit = "no"

while userExit != "yes":
  animal = input("Which animal do you want to hear their sounds?: ")
  if animal == "Cow" or animal == "cow":
    print("A cow goes moooo 🐮")
  elif animal == "dog" or animal == "Dog":
    print("A doggie goes woof woof 🐶🐶")
  elif animal == "horse" or animal == "Horse":
    print("A horse goes neighhhhh 🐴🐴")
  elif animal == "cat" or animal == "Cat":
    print("A cat goes meowww 😺")
  else:
    print("Apologies but we do not have the sound for that animal.")
  print()
  userExit = input("Do you want to quit the program?: ")
  print()
