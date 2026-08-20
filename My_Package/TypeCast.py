item =  input("what item would you like to buy:")
price = float(input ("what is the price of the item:"))
quantity = int(input("How many would you like?"))
total = price * quantity
print(total)
print(f"you have bought {quantity} X  {item}/s")
print (f"your total is: ${total}")
