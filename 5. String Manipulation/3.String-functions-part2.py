a= "Hello"
b="Hello1234"
c="123456"
d="HELLO"
e= " "
f= "Hello 123"
g= "1.234"


#is strings are alphanumeric
print(c,c.isalnum())  
'''space isn't alphanumeric'''
print(e,e.isalnum()) 
print(g,g.isalnum()) 



#strings are only alphabets

print(a, a.isalpha())


#is decimal?

print(c, c.isdecimal())


#is digit?

print(c, c.isdigit())



# are numeric?

print(b, b.isnumeric())


#check if the string is lowercase/uppercase or not

print(a, a.islower())
print(a, a.isupper())


#whitespaces?

print(e, e.isspace())
print(f, f.isspace())


#title?

print(a, a.istitle())