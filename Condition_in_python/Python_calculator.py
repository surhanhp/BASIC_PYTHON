operators = input("Enter the operatora:(+,-,*,/):")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
if operators == "+":
    result = num1 + num2
    print(round(result,3))
elif operators == "-":
        result = num1 - num2
        print(round(result,3))
elif operators == "*":
            result = num1 * num2
            print(round(result,3))
elif operators == "/":
                result = num1 / num2
                print(round(result,3))
else:
    print(f" the {operators} operator is invalid")