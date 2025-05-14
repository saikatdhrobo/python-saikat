operator = input("enter and operator: (+ - * /): ")
num1 = float(input("Enter the 1st no.: "))
num2 = float(input("Enter the 2nd no.: "))

if operator == "+":
    result = num1 + num2
    print (round(result,3))

elif operator == "-":
    result = num1 - num2
    print (round(result,3))

elif operator == "*":
    result = num1 * num2
    print (round(result,3))

elif operator == "/":
    result = num1 / num2
    print (round(result,3))  # দশমিকের পরে তিনঘর

else:
    print(f"{operator} is an Invalid operator")