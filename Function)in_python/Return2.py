def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" " + last

whole_name = (create_name("surhan","halepoto"))
print(whole_name)

def greet(name = "Koi be"):
    print("Hello,",name)
greet("surhan")
greet()
#* ARGS JAB PATA NA HO KON SI VALUE DENI HE .
def add_all(*numbers):
    total =0
    for n in numbers:
        total += n
    return total
print(add_all(1,2,3,4,5,6,7,8,9))
print(add_all(20,5,15,10))
print(add_all(100))


