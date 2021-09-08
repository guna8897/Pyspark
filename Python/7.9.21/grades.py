for i in range(0,100):
    grade = float(input("Enter the Mark"))
    if grade >= 80:
        print("Your grade is A")
    elif 60 <= grade < 80:
        print("Your grade is B")
    elif 40 <= grade < 60:
        print("Your grade is C")
    else:
        print("Your grade is D")