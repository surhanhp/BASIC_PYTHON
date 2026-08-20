students = {"ali":89,"father":96,"mother":35,"sister":78,"brother":27}
for name,marks in students.items():
    if marks > 50:
        print(f"{name} has {marks} marks")
    #print(f"key is {name} : and marks is value  {marks}%")