# define a function
lecname = ""
unit = ""

def scheduler():
    lec_hall = input("Enter Lecturer Hall\n")
    time = input("Enter the time\n")
    day = input("Enter time of the day\n")


    # is there a time data type? datetime()

    if lec_hall == "TH" and time == "8:00-11:00" and day == "Monday":
        lecname = "James"
        unit = "Database Systems"
        flag = 1
    elif lec_hall == "OH" and time == "14:00-17:00" and day == "Thursday":
        lecname = "Kioko"
        unit = "Artificial Intellgence"
        flag = 1
    else:
        flag = 0

    if flag == 1:
        print(lecname,"\n",unit, "\n")
    else:
        print("Student has no class at the time\n")


scheduler()
