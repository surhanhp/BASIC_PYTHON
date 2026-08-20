number = int(input("Enter a number of table: "))
table = 1
while table <= 10:
    result = number * table
    print(table,"*",number,"=",result)
    table += 1