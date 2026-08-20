Number = int(input("Enter a number: "))
if Number <= 1:
    print("This is not a prime number")
elif Number == 2:
    print("This is  a prime number")
elif Number % 2 == 0:
    print("This is not a prime number")
else:
    print("This is  a prime number")
