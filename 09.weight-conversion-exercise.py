weight = float(input("Enter your weight: "))
unit = input("KG or Pounds? (K or L)")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lb"
    print(f"Your weight is: {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight / 2.20462
    unit = "kg"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid! Try again.")
