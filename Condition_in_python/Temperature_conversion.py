unit = input("is this temperature in celcius or fahrenheit? (C/F) :")
temp = float(input("Enter your temperature "))
if unit == "C":
    temp =round((9 * temp)/5 + 32,1)
    print(f" The temperature in fahrenheit is {temp}°F ")# alt+0176=°
elif unit == "F":
    temp = round((temp-32) *5/9,1)
    print(f"The temperature in celcius is {temp}°C")
else:
   # print(f"Your temperature is: {temp}")
    print(f"{unit} your unit is not valid for measurment")