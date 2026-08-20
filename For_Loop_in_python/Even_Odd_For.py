limit = int(input("Enter a limit: "))
for count in range(1, limit):
    if count % 2 == 0:
     print(count)
    count = count + 2

print("___ODD NUMBER___")
for num in range(1, limit):
    if num % 2 == 1:
        print(num)
        num = num + 2
