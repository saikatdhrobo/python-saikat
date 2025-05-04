a= "Harry Potter and the Goblet of Fire"
print(a)

#find length of string
print(len(a)) 

#find the number of times a character is occuring
print(a.count("o"))

#to convert each letter into uppercase

print(a.upper())


#to convert each letter into lowercase

print(a.lower())



#to find the index(position) of any character

print(a.index("o"))

#to find the index(position) of any character between a range

print(a.index("o",15,34))


#Capitalize the first letter of sentence

print(a.capitalize())

# every first letter will be small letter
print(a.casefold())



#find the index no. of a character

print(a.find("o",15,34))



#format method
name = "Saikat"
b = "My name is {} and my age is {}"
age =24
print(b.format(name,age))



#it fills the given characters and centralizes a string

print(name.center(20,"*"))