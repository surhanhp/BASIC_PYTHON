person = {"name" : "Ali",  "city" : "New York"}
person["age"] = 20
person["address"] = 10
person["city"] =  "Karachi"
print("Before delete :" , person)

del person["name"]
print("after delete" , person)