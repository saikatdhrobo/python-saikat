"""Basics of if-elif-else"""


# if = do some code only if some condition is true
# elif = do some code if the condition is not true but some other condition is true
# else = else do something else

age = int(input("enter your age: "))

if age>=18:
    print("You're signed up!")

elif age<=0:
    print("You haven't been born yet!")
elif age>= 100:
    print("You are too old to sign up.")

else:
    print("You must be 18+ to sign up")





"""Another example to learn"""


response = input("Would you like food? (Y/N)")
if response == "Y" or response == "y":
    print("Here is your food!")
else:
    print("No food for you!🤣")




"""Other example to learn"""

name = input("Enter ur name: ")

if name=="":
    print("you didn't type ur name")
else:
    print(f"Hello {name}")




"""Use boolean with if statements(1)"""

for_sale = True

if for_sale:
    print("This item is for sale!")

else:
    print("This isn't for sell")



"""Use boolean with if statements(2)"""

online = False

if online:
    print("You are online")
else:
    print("You are offline")