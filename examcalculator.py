CAT = int(input("enter CAT Marks\n"))
#how to include validation

MainExam = int(input("enter Main Exam Marks\n"))
FinalScore = CAT + MainExam
print(FinalScore)

if FinalScore <= 50:
    print("you have failed the examinations")
elif FinalScore > 50:
    print("you have passed the examination")
