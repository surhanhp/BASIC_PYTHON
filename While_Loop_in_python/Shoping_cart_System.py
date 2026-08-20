cart = []
item = input("Enter your items:")
while item != "done":
 cart.append(item)
 item = input("Enter your items:")
print("Your cart :",cart)
print("Total Items: ",len(cart))