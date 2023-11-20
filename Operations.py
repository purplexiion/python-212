"""
Membership Operators - include in and not in
example: if x in y
if x not in y

typecasting: converting one variable from one data type to another
done using constructor functions e.g. int(), float(), str e.t.c
"""

# Question 1
Number = int(input("Insert number a\n"))
rem = Number%2
if rem == 0:
    print("the number is an even number")
else:
    print("the number is an odd number")

# Question 2
Principal = int(input("Insert the Amount of Money\n"))
Years=int(input("Insert the duration of the period in years\n"))
Rate = 16

NewAmount = int(Principal * (Rate/100 + 1)**Years)
Interest = NewAmount - Principal
print("New Amount:\n",NewAmount)
print("Interest Generated:\n",Interest)
print("The following amount", NewAmount,"was generated with a principal of",Principal,"at a rate of",Rate,"% in a duration of",Years,"years")


# Question 3
AdmNo = int(input("Enter Admission Number"))
StdName =str(input("Enter Student Name"))
UnitCode =str(input("Enter unit code"))
UnitName = str(input("Enter Unit Name"))
CAT = int(input("Input CAT Marks"))
MainExam =int(input("Input Main Exam Marks"))

FinalScore = MainExam + CAT
print(FinalScore)

if FinalScore > 70:
    Grade="A"
elif FinalScore >= 60:
    Grade="B"
elif FinalScore >= 56:
    Grade="C"
elif FinalScore >= 50:
    Grade="D"
else :
    Grade="F"

print("Student Name\t",StdName)
print("Unit Code\t",UnitCode)
print("Unit Name\t",UnitName)
print("Final Score\t",FinalScore)
print("Grade\t", Grade)

