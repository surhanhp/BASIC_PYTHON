# FUNCTION:: A BLOCK OF REUSABLE CODE PLACE () AFTER THE FUNCTION NAME TO INVOKE IT.
def happy_birthday(name,age):
    print(f"Happy Birthday Toooooo  youuuuuuuuuuuu  {name}:")
    print(f"you are {age} years old")
    print()
happy_birthday("bro", 20)
happy_birthday("Ali",28)

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"You have ${amount :.2f}  on a due: {due_date} ")
display_invoice("surhan",100.02,"22/07/2026")