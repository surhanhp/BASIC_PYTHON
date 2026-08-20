       # BODY MASS INDEX  CALCULATOR   #
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight / (height ** 2)
if bmi > 18.5:
    print("Underweight. your bmi is",bmi)
elif bmi <= 24.5:
    print("Normal. your bmi is",bmi)
else:
    print("Overweight. your bmi is",bmi)