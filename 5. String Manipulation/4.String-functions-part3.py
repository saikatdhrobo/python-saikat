#string ends with specified value

a= "Harry Potter"
print(a.endswith("t",6,9))




#string starts with specified value
a= "Harry Potter"
print(a.startswith("H",0,5))




#Swapcase - lower become upper, upper become lower

a= "Harry Potter"
print(a.swapcase())






#trimming version of string

a="   Harry Potter   "
print(a)
print(a.strip())



#separate/split string from particular value

a ="#00FD#BRB#2MW"
print(a.split("#"))




#left justified
a="Harry Potter"
x=a.ljust(20)
print(x, "is my fav movie")


#rjust gives right justified string
a="Harry Potter"
x=a.rjust(20)
print(x, "is my fav movie")




#replace 

a= "My name is John"
print(a.replace("John","Saikat"))




#rindex()

a= "Harry Potter and the Prisoner of Azkaban"
print(a.rindex("Prisoner"))



#rfind()

a= "Harry Potter and the Prisoner of Azkaban"
print(a.rfind("Prisoner"))