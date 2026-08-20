## Acess karna
student = {"name":"Ayesha","age":54,"field":"data science"}
student["name"]
student.get("name")
#print(student.get("city","Not found"))
#UPDATE/ADD KARNA
student["city"] = "Lahore"
student["age"] = 22
print(student)
#DELETE/POP KARNA
del student["city"]
student.pop("age")
student.popitem()#last inserted pair delete karta  he .popitem()
student.clear()
print(student)