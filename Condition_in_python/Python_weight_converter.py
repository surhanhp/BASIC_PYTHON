weight = float(input("Enter your weight: "))
unit = input("It is kilogram or pounds (K or L) :")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
   # print(f"Sorry, {unit} is not a valid unit.")
    print(f"Your weight is: {weight} {unit}")

