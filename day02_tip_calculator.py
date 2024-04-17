print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $ "))
percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

totalPerPerson = (bill + ((bill * percentage) / 100)) / people
finalAmount = "{:.2f}".format(totalPerPerson)

print(f"Each person should pay: ${finalAmount}")