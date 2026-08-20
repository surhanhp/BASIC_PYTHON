menu = {"pizza":3.00,
        "chicken":1.00,
        "burger":12.00,
        "samosa":50.0,
        "chips":70.0,
        "fries":65.00,
        "soda":80.00}
cart = []
total = 0
print("_________MENU__________")
for key,values in menu.items():
    print(f"{key :}:${values:.2f}")
print("____________________________")
while True:
 food = input("Selected an item:(q to quit):").lower()
 if food == "q":
     break
 elif menu.get(food) is not None:
     cart.append(food)
print(cart)
print("__________   YOUR ORDER  ______________")
for food in cart:
    total += menu.get(food)
    print(food,end="")
print()
print(f"total is : ${total:.2f}")