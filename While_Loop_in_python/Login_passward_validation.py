correct_password = 787426

attempt = 3
while attempt <= 3:
  user_pin = int(input("Enter your PIN: "))
  attempt = attempt + 1
if user_pin == correct_password:
     print("your PIN is correct")

else:
    print("your PIN is incorrect")