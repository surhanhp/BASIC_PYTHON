bill = float(input("Enter your bill: "))
if bill > 5000:
    discount = bill * .20
elif bill >=2000:
    discount = bill * 0.10
else:
    discount = 0
final_amount = bill - discount
print("Discount: ",discount)
print("Final amount to pay:",final_amount)