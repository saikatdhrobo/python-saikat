#1.Write a program to display a person's name, age and address in three different lines.

name="Saikat"
age = 23
address ="Narsingdi"

print(name)
print(age)
print(address)


#2.Swap to variables

'''Method 1'''

x=12
y=13
temp=x
print(temp)
x=y
print(x)
y= temp
print(y)
print("value of x is:",x)
print("value of y is:",y)

'''Method 2'''

a=30
b=40
a,b=b,a #left,right=right,left
print("Value of a and b after swapping is:", a,b)



#3. Convert a float into integer.

a = 22.28
print("Integer value is: ", int(a))


#4. Take details from a student for ID Card and then print it in different lines

name = input("Enter name of the student: ")
age = int(input("Enter age: "))
grade = float(input("Enter grade: "))
email= input("Enter e-mail: ")

print("Student ID Card Details:")
print("Name:",name)
print("Age:",age)
print("Grade",grade)
print("Email:", email)



# 5. Take user input as integer and convert to float

integer_Number = int(input("Give a integer number:"))
print("Float number is:", float(integer_Number))