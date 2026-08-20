#def find_max(*numbers):
#list = {12,45,89,26,67}
def find_max(*numbers):
 maximum = numbers[0]
 for num in numbers:
    if num > maximum:
        maximum = num
 return maximum
print(find_max(66,67,654,78,10,6988.))