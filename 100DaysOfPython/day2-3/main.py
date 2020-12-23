# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
MaximumAge = 90

yearsLeft = MaximumAge - int(age)
monthsLeft = 12*yearsLeft 
weeksLeft = 52 * yearsLeft
daysLeft =  365 * yearsLeft


print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months left ")

