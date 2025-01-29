"""print("Press 1 to Covert Fahrenheit to Celcius")
print("Press 2 to Covert Celcius to Fahrenheit")
choice = int(input())
if choice == 1:
    F = float(input("Enter Fahrenheit: "))
    print (((F-32)*5/9))
else:
    C = float(input("Enter Celcius: "))
    print (((C*9/5)+32))"""

import math
def fun(x):
  #Enter your Equation
  p = ((5*x**3)-5*(math.cos(x))-8)
  return p

x1 = float(input("Enter value of a: "))
x2 = float(input("Enter value of b: "))
print("\nBisection Solution: ")
i = 0
tmp = 1e5
while True:
  print("\n\n")
  print("Step: ",i+1) ; i+=1
  print("a = ",round(x1,3))
  print("b = ",round(x2,3))
  print("f(a) = ", round(fun(x1),3))
  print("f(b) = ", round(fun(x2),3))
  c = (x1+x2)/2
  print("c = ",round(c,3))
  print("f(c)= ",round(fun(c),3))
  if round(c,3) == round(tmp,3):
    break
  else:
    tmp = c
  if (fun(x1) * fun(c)) <= 0:
    x2 = c
  else:
    x1 = c