print("GRADEBOOK 📔📔")
print()
testName = input("What is the name of your test?: ")
maximumScore = int(input("What is the maximum score attainable in the test?: "))
userScore = int(input("What is your score?: "))
percentageGrade = (userScore/maximumScore) * 100
percentageGrade = round(percentageGrade, 2)

print()
if percentageGrade >= 90:
  print("An A+, congratulations, I'm so proud of you 🥳🥳")
elif percentageGrade >= 80 and percentageGrade <= 89:
  print("Wow 😲😲 you got an A, congrats yo 🤝")
elif percentageGrade >= 70 and percentageGrade <= 79:
  print("You got a B, congratulations, you did good 😁😁")
elif percentageGrade >= 60 and percentageGrade <= 69:
  print("Not bad, not bad, You got a C, welldone 😊😊")
elif percentageGrade >= 50 and percentageGrade <= 59:
  print("Yooo, you got a D 😬😬, the important thing is that you managed to pass, please do better, I know you can 👍👍")
else:
  print("Omo a U, that's bad, but life happens, as someone who has been there, I know you'll be fine, don't let it get to you 🫂🫂")

print("Percentage grade:", float(percentageGrade))
