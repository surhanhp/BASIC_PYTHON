Capitals = {"Sindh":"Karachi","Peshawar":"Quita","Pakistan":"Islamabad"}
#print(dir(Capitals))
#print(help(Capitals))
print(Capitals.get("Sindh"))
if Capitals.get("Sindh"):
    print("That capital is exists:")
else:
    print("That capital is not exists")
Capitals.update({"KPK":"balochistan"})
Capitals.pop("Sindh")
#Capitals.clear()
print(Capitals)
for key,value in Capitals.items():
    print(f"{key}:{value}")
items = Capitals.items()
print(items)
values = Capitals.values()
print(values)
keys = Capitals.keys()
print(keys)