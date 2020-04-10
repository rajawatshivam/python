#salaryCleanup

rawData = input("Enter the salary: ")
salary = rawData.replace('$','')
salary = salary.replace(',','')
print ("Your salary is :",salary)