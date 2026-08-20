#.KEY()
family = {"mother":"hoor","father":"sadique","brother":"sabir"}
for k in family.keys():
    print(k)
print(family.keys())
#.VALUES()
for V in family.values():
    print(V)
print(family.values())
#.ITEMS() HIN MEN KEY AND VALUE BOTH
for key,value in family.items():
 print(key,value)
print(f"This is our family {key}  {value}")