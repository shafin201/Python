id = input("Enter Employee ID : ")
work = float(input("Total worked Hour of the Month : "))
amnt = float(input("Per Hour Amount : "))

salary = work*amnt

print("Employee ID : ",id)
print("Salary of the Month  : ",round(salary,2) ,"BDT")


