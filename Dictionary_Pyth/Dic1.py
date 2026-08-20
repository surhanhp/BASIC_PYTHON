data = {"Alice":1.53, "Bob":20.25, "Charlie":0.243}
data["Alice"] = 2.05654
print(data.get("Ali","Not Found:"))
class_marks = {"ali":85,"bro":89,"charlie":41,"sister":35,"mother":78,"father":97}
for name,marks in class_marks.items():
    if marks > 50:
        print(f"Wow you got 50% {marks}")
    else:
        print(f"Sorry you can't get possible {marks}")
    print(f"your name is {name} and you got a {marks}% marks")
