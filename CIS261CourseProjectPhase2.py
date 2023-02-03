#   Kristine Jenkins
#   CIS261
#   Project Phase 2

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start date (mm/dd/yyyy): ")
    todate = input("Enter End date (mm/dd/yyyy): ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print()
        print("Name: ", empname)
        print("From Date: ", fromdate)
        print("To Date: ", todate)
        print("Hours Worked: ", f"{hours:,.2f}")
        print("Hourly Rate: ", f"{hourlyrate:,.2f}")
        print("Gross Pay: ", f"{grosspay:,.2f}")
        print("Tax Rate:  ", f"{taxrate:,.1%}")
        print("Income Tax: ", f"{incometax:,.2f}")
        print("Net Pay: ", f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay


def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHours"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')


if __name__ == "__main__":
   
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)

    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)


