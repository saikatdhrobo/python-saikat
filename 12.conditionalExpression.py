# 1 line shortcut for if-else statements (ternary operator)

# X if condition else Y

"""example 1"""
num = -5
print("Positive" if num > 0 else "Negative")


"""example 2"""
num = 6
result = "even" if num%2==0 else "odd"
print(result)



"""example 3"""
a = 6
b = 7
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)



"""example 4"""
temperature = 10
weather = "hot" if temperature >20 else "cold"
print(weather)