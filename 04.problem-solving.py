#1. Write a program to display a person's name, age and address in three different lines.

name = "Saikat"
age = 23
address = "Narsingdi"
print(name)
print(age)
print(address)


#2. Write a program to swap two variables
# method-1
x= 12
y=13
temp = x
print(temp)
x=y
print(x)
y= temp
print(y)
print ("Value of x is: ", x)
print ("Value of y is: ", y)


#method-2
a= 30
b=40
a,b=b,a #left=right,right=left
print("Value of b is: ",b)
print("Value of a is: ",a)


#3. Write a program that convert a float into integer
num = 45.67
print(int(num))


##4. Write a program to take details from a student for ID-card and then print it in different lines.

name= input("Enter your name:")
age = int(input("Enter your age:"))
grade = input("Enter your grade:")
email= input("Enter your email:")
phone_number = input("Enter your phone number:")
print("Student Identity Card")
print(name)
print(age)
print(grade)
print(email)
print(phone_number)


#5. Write a program to take an user input as integer then convert it to float.

a= int(input("Enter a number:"))
print(a)
print(type(a))
a = float(a)
print("after conversion", a)
print(type(a))