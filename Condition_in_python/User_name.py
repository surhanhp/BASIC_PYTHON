user_name = input("Enter your name: ")
if len(user_name) > 12:
    print("your user name can not be longer than 12 characters:")
elif not user_name.find(" ")== -1:
    print("your user name can not contain spaces:")
else:
    print(f"wellcome{user_name}")