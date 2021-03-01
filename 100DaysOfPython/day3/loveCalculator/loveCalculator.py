# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_test = "true"
love_test = "love"
true_count = 0
love_count = 0

for letter in name1:
  true_count += true_test.count(letter.lower())

for letter in name2:
  true_count += true_test.count(letter.lower())
 


for letter in name1:
  love_count += love_test.count(letter.lower())

for letter in name2:
  love_count += love_test.count(letter.lower())

print( f"Your scoree is {true_count}{love_count} ")

 

 
