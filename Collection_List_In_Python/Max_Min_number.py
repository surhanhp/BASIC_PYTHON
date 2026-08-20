numbers = [23,28,85,78,69,344]
biggest = 0
smallest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
        if num < smallest:
            smallest = num
print("Biggest number is :",biggest)
print("Smallest is :",smallest)