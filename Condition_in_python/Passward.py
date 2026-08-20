password = input("Enter your password: ")
if password == "123456":
    print("Password is valid")
elif password == "admin2004":
    print("Password is valid for admin .")
else:
    print("Password is not valid")

password = input("Enter your password: ")
valid_password = ["123456","admin2004"]
if password in valid_password:
    print("Password is valid")
else:
    print("Password is not valid")
