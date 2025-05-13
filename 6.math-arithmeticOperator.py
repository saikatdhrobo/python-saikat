"""Arithmetic Operators"""

a = 0
b = 1
c = 2
d = 4

a += 1
b -= 2
c *= 3
d /= 2
d = d ** 2
remainder = d % 3

print(a)
print(b)
print(c)
print(d)
print(remainder)


"""Math Functions"""

x = 3.14
y = -4
z = 5

result = round(x) #round function
print(f"Round of x is: {result}")
print(f"Absolute value of y is: {abs(y)}")
print(f"max value is: {max(x, y, z)}")
print(f"min value is: {min(x, y, z)}")
p= 2
q = 3
power = pow(p,q)
print(f"Power of p and q is: {power}")






"""Import math functions"""

import math

x = 16
y= 16.5
print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(y))
print(math.floor(y))






"""Circumference of circle"""

import math

radius = input("enter the radius: ")
circumference = 2 * math.pi * float(radius)

print(f"The circumference is : {circumference}cm")



"""Area of circle"""

import math
radius = input("enter the radius:")
area = math.pi * (float(radius))**2
print(f"The area is: {area}cm")