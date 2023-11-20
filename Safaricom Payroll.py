basicpay = float(input("Insert the amount of salary you earn \n"))
overtime = int(input("Insert the number of overtime hours \n"))
NSSF = 80.00
NHIF = 200.00
ServiceCharge = 100.00

# finding the overtime hours
if 0 < overtime <= 50:
    overtimepay = overtime * 300
if overtime > 50:
    overtimepay = (50 * 300) - (overtime - 50) * 350
# Finding gross salary
gsalary = overtimepay + basicpay
# Finding the PAYE given
if gsalary >= 50001:
    paye = 0.14 * gsalary
elif 40000 <= gsalary < 50000:
    paye = 0.12 * gsalary
elif 35000 <= gsalary < 39999:
    paye = 0.11 * gsalary
elif 25000 <= gsalary < 34999:
    paye = 0.08 * gsalary
elif 16000 <= gsalary < 24999:
    paye = 0.05 * gsalary
elif 9500 <= gsalary < 15999:
    paye = 0.03 * gsalary
else:
    paye = 0
# Finding the net pay
deductions = paye + NHIF + NSSF + ServiceCharge
netpay = gsalary - deductions
print("Overtime Pay", "Gross Salary", "Net Pay", "PAYE")
print(overtimepay, "\t", gsalary, "\t", netpay, "\t", paye)
