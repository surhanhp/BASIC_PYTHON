questions = ("How many elements in periodic table?",
             "Which elements lays the largest egg?",
             "Which is the most abundant gas in earth's atmosphere?",
             "How many bones in human body?",
             "Which planet in solar system is hottest?")

options = (("A.116","B.117","C.118","D.181"),
           ("A.whale","B.crocodile","C.Elephant","D.Butterfly"),
           ("A.Methan","B.Nitrogen","C.Oxygen","D.Carbon_di_oxide"),
           ("A.126","B.206","C.260","D.306"),
           ("A.venus","B.Jupiter","C.Mars","D.Earth"),)
answers = ("C","D","B","B","A")
guesses = [ ]
score = 0
question_num = 0

for question in questions:
    print("____________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer!C")

    question_num += 1

print("____________________________")
print("         RESULT!            ")
print("____________________________")

print("answers:", end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess,end=" ")
print()
score = (score/len(questions) * 100)
print(f"Your final score is: {score}%")

