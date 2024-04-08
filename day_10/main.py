print("BILL CALCULATOR 🤑🤑")
print()
myBill = float(input("What was the bill?: "))
tipAmount = int(input("How many percent do you want to tip?: "))
totalBillAmount = ((tipAmount * myBill)/100) + myBill
numberOfPeople = int(input("How many people?: "))
billPerPerson = totalBillAmount / numberOfPeople
billPerPerson = round(billPerPerson, 2)
print()
print("You all owe", billPerPerson)