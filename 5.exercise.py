"""1. Area and Volume calculate"""

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = length * width
volume = length * width * height
print(f"The area of the rectangle is: {area} cm^2")
print(f"The volume of the rectangle is: {volume} cm^3")




"""2. Shopping Cart"""

item = input("What item would u like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would u like? "))

total = price * quantity

print(f"You have bought {quantity} {item}(s) for total ${total}")