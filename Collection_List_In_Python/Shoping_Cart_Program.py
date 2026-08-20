foods = []
prices = []
total = 0
while True:
    food = input("Please enter your food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter a price of food is {food} $"))
        foods.append(food)
        prices.append(price)
print("______ YOUR CART ______ ")
for food in foods:
    print(food)
