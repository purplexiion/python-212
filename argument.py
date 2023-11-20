# using an arbitrary set of arguments
def grades(*grade):
    print("Third Grade", grade[2])


grades("A", "B", "C", "D", "E", "F")


# keyword arguments
def my_name(sname, oname):
    print("full names are:", sname + oname)


my_name(oname="John", sname="Cena")


# default arguments
def my_country(name, country="Kenya"):
    print("i am called\t" + name + "and I am proud to be from" + country)


my_country("Wamuyu", "Kosovo")
my_country("Wachira")
my_country("Millie", "United States of America")

#   lambda functions
y = lambda a, b, c: a + b + c
# don't use the print function in the lambda function
print("the sum of three numbers is", y(1, 2, 4))

'''
# using an if statement
no = lambda c,d,e:
    if c>d:
        print("c is greater than d and e" 
    elif d>e:
        print("d is greater than e and c")
    else:
        print("e is greater than d and c")

no(2,3,4)
 '''
# using the max function
maxno = lambda no1, no2, no3: max(no1, no2, no3)
print(max(90, 100, 872))


def payrollautomation():
    # enter the employee details
    employeename = input("enter employee name")
    gender = input("enter your Gender")
    jobgrade = input("enter your jobgrade")

    print(employeename, gender, jobgrade)
    # determine what each person gets as their basic salary based on their grade
    if jobgrade == "H":
        basicsal = 12000
        houseallow = 2000
        travelallow = 3000
    elif jobgrade == "M":
        basicsal = 18000
        houseallow = 0
        travelallow = 0
    else:
        basicsal = 60000
        houseallow = 40000
        travelallow = 12000

    print(jobgrade, basicsal, houseallow, travelallow)

    grosssal = basicsal + houseallow + travelallow

    print("this is the gross salary", grosssal, "for the employee called" + employeename)


payrollautomation()
