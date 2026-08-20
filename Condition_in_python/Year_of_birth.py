birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
if age >= 18 and age <= 35:
    print("you are adult:")
elif age >= 40:
    print("You have becoming the father🥰")
else:
    print("you are teenager:")