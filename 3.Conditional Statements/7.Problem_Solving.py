#1. Write a program to check if a number is positive

num = float(input("Enter a no.:" ))
if num >0:
    print("It's positive")
else:
    print("It's negative")




#2. Check number is odd or even

num = float(input("Enter the number:"))
if num%2==0:
    print("It's even no.")
else:
    print("It's odd no.")




#3. To create a area calculator

print("___Area Calculator___")
print("""Press 1 to get area of square:
Press 2 to get area of rectangle:
Press 3 to get area of circle:
Press 4 to get area of triangle:  """)

choice = int(input("Enter a number between 1 to 4:"))

if choice ==1:
    side = float(input("enter the length of oneside:"))
    area= side**2
    print("The area of square is:",area)

elif choice==2:
    length = float(input("Enter the length:"))
    width = float(input("Enter the width:"))
    area = length*width
    print("The area of Rectangle is:",area)

elif choice==3:
    radius = float(input("Enter the radius:"))
    area=3.1416* radius**2
    print("The area of circle is:",area)

elif choice==4:
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    area= 0.5*base*height
    print("The area of triangle is:",area)

else:
    print("Invalid Input")





#4. Check passed letter is vowel or not


letter = input("Enter a letter: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It's a vowel")
else:
    print("It's not vowel. It's consonant")





#5. check if number is single digit,double digit and so on...upto 5 digits

num = int(input("Enter a number upto 5 digits: "))

if num <= 9 and num >= 0:
    print("Single Digit")
elif num <= 99 and num >= 10:
    print("Double Digit")
elif num <= 999 and num >= 100:
    print("Triple Digit")
elif num <= 9999 and num >= 1000:
    print("Four Digit")
elif num <= 99999 and num >= 10000:
    print("Five Digit")
else:
    print("Other digit")
