# converts datatype one to another is TypeCasting

#explicit typecasting

name = "Saikat"
age = 23
gpa =3.21
student = True
place =""

"""lets check datatype of these variables"""
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

"""now lets convert datatype of these variables using explicit"""

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))


student = str(student)
print(student)
print(type(student))



place = bool(place)  #it will show false, as null and zero value is false
print(place)
print(type(place))






#implicit typecasting (automatically change datatype)

x = 2
y = 2.0
x= x/y

print(x)