#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip  = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

amtOfPeopleSplitting  = int(input("How many people to split the bill?  "))

totalBill = bill + (bill * tip/100)
sharingCost = round(totalBill/amtOfPeopleSplitting, 2)

print(f"Each person should pay: {sharingCost}")
