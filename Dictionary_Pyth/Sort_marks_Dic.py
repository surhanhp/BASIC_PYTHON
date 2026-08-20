students = {"A":90,"C":89,"E":95,"G":79,"B":97,"D":49,"R":59}
top_student = ""
top_marks = 0
for name,marks in students.items():
    if marks > top_marks:
        top_student = name
        top_marks = marks
print(top_student,"has the highest marks",top_marks)