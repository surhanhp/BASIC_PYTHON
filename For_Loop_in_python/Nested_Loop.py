#NESTED LOOP :  A LOOP WITHEN AN OTHER LOOP (OUTER , INNER)
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")
for x in range(rows):
    for y in range(columns):
      print(symbol,end=" ")
    print()


#for x in range(4):
   # for y in range(1,11):
     # print(y,end=" ") # DONOT GO TO NEXT LINE PRINT ON THAT LINE.
    #print()
