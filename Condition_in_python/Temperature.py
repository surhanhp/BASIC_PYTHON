Temperature = float(input("Please enter your temperature in Celsius:"))
if Temperature <= 0:
    print("Freezing")
elif Temperature <= 15:
    print("Cold")
elif Temperature <= 25:
    print("Moderate")
else:
    print("Hot")
