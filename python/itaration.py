import math
def g1(c):
  #p = abs(math.sin(c)/2)
  #p = 0.5*(math.cos(c)+3)
  #p = 1/(math.sqrt(x+1))
  p = (math.sin(c)-8)/5
  #p = math.sqrt(abs(math.sin(c)-10/90))
  return p

i = 0
x = float(input("Enter initial (3.2 or 0.5): "))
print("Fixed point Iteartion Solution: ")
while True:
  print("\n")
  print("Step ", i+1)
  print("X",i," = ", x); i+=1
  v = round(g1(x),3)
  if v == x:
    print("\n")
    print("Step ", i+1)
    print("X",i," = ", x)
    break
  else:
    x = v

"""def fun(x):
  p = ((5*(x**3))+2*(x)-8)
  return p

x1 = float(input())
x2 = float(input())
print("False Position Solution: ")
i=0
for var in range (8):
  print("\n\n")
  print("Step: ",i+1)
  i+=1
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
    x2 = x3"""