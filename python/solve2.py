
"""def Fehrenheit(f):
    res = (f*9/5)+32
    return round(res,3)
def Celcius(c):
    result = (c-32)*5/9
    return round(result,3)
f=float(input("Enter Temperature: "))
print("Fahrenheit Temperature is = ",Fehrenheit(f))

c = float(input("Enter Temperature: "))
print("Celcius Temperature is = ", Celcius(c))"""




"""fharenhigt = float(input("Enter Temperature :"))
celsiaus = (fharenhigt - 32)*5/9
print("Celsiaus is :",celsiaus)


celsiaus = float(input("Enter Temperature :"))
fharenhigt = (fharenhigt + 9/5)+32
print("Fharenhigt is :",fharenhigt)"""

ID = input("Enter employee ID: ")
Workhour= float(input("Enter Workhour of a day: "))
Amount =  float(input("Enter per hour  amount: "))

Workhour_of_a_month = Workhour*22  #According to formal workhour including two offday (friday & saturday)
salary = Workhour_of_a_month * Amount


print("Employee ID: ", ID)
print("Salary of the whole month: ",round(salary,2))