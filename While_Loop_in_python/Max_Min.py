
count = 1
max_num = 0
min_num = 0
while count <= 3:
    num = int (input("Enter a number:"))
    if count == 1:
        max_num = num
        min_num = num
    else:
        if num > max_num:
            max_num = num
            if num < min_num:
                min_num = num
                count = count + 1
        print("maximum number is :",max_num)
        print("minimum number is :",min_num)
