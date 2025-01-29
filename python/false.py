import math
def fun(x):
  #Enter your Equation
  p = 2*(x**2)+x-8
  return p

x1 = float(input("Enter value of x1: "))
x2 = float(input("Enter value of x2: "))
print("False Position Solution: ")
i = 0
while True:
  print("\n\n")
  print("Step: ",i+1) ; i+=1
  print("x1 = ",round(x1,3))
  print("x2 = ",round(x2,3))
  print("f(x1) = ", round(fun(x1),2))
  print("f(x2) = ", round(fun(x2),2))
  x3  = x1 - (((x2-x1)*fun(x1))/(fun(x2)-fun(x1)))
  print("x3 = ",round(x3,3))
  print("f(x3)= ",round(fun(x3),3))
  if round(x1,3) == round(x3,3):
    break
  if fun(x3) < 0:
    x1 = x3
  else:
    x2 = x3