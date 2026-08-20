number = int(input("Enter a number: "))
for number in reversed(range(0 , number)):
    if number == 5:
      continue
    print(number)