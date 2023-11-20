time = input("Enter time for travel")
des = input("enter destination for travel")

if time == "11:00" and des == "Voi":
    vregno = "KBZ 009Z"
    arrtime = "12:00pm"
    fare = 300.00
    flag = 1
elif time == "9:00" and des == "Kisumu":
    vregno = "KBX 100X"
    arrtime = "12:00am"
    fare = 3400.00
    flag = 1
elif time == "8:00" and des == "Mombasa":
    vregno = "KAQ 998Y"
    arrtime = "2:00am"
    fare = 3500.00
    flag = 1
else:
    flag = 0

if flag == 1:
    print("There is a car available")
    print(vregno, arrtime, fare)
else:
    print("there is no car available")
