unit = (input("The temperature unit: (C/F): "))
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature= round((temperature * 9/5) + 32 ,2)
    print(f"The temperature in Fahrenheit is {temperature} °F")

elif unit == "F":
    temperature = round((temperature - 32) * 5/9 ,2)
    print(f"The temperature in Celsius is {temperature} °C")

else:
    print(f"The {unit} is an Invalid unit of measurement")