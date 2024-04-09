print("How many seconds are in a year 😊😊")
print()
leapYear = input("Is this year a leap year, answer y for YES and n for NO: ")
if leapYear == "y":
    numberOfDays = 366
    secondsInAYear = (60*60*24*numberOfDays)
    print()
    print("The number of seconds in a year is", secondsInAYear)
elif leapYear == "n":
    numberOfDays = 365
    secondsInAYear = (60*60*24*numberOfDays)
    print()
    print("The number of seconds in a year is", secondsInAYear)
else:
    print("That is not one of the suggested options.")

