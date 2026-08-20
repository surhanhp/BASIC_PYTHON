#RETURN FUNCTION
def add (a,b):
    c = a+b
    return c
def add(*args):
    total = 0
    for n in args:
        total += n
    return total
print(add(1,2,3,4))
def subtract(a,b):
    c = a-b
    return c
def multiply(a,b):
    c = a*b
    return c
def divide(a,b):
    c = a/b
    return c
print(add(10,20))
result = (add(10,20))
print(result * 2)
print(subtract(10,7))
print(multiply(5,10))
print(divide(10,3))