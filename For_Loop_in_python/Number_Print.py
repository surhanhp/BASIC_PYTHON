number = int(input("Enter a number: "))
for number in range(0 , number):
    if number == 5:
       # break
      continue
    print(number)
print("----REVERSE NUMBER----")

number1 = int(input("Enter a number: "))
for number1 in reversed(range(0 , number1)):
    if number1 == 5:
      continue
    print(number1)
