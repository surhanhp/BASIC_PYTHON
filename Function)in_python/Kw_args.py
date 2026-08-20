def print_address(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
print_address(street="123 Fake.st",
              city="Tando Bago",
              state="UK",
              zip="54321",
              country="Pakistan")
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    print(f"{kwargs.get('street')} , {kwargs.get('city')} , {kwargs.get('zip')}")

shipping_label("Dr.","Surhan","Halepoto","III",
               street="123 Fake.st",
               apt= "100",
               city="Tando Bago",
               state="UK",
               zip = "54321",
               country="Pakistan")

