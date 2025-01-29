import math
def f(x):
    p = (x**3)+math.cos(x)-3
    return p

def f1(x):
    p = (3*(x**2)-math.sin(x))
    return p

x = float(input())
print("Newton rapson Solution: ")
i = 0
while True:
    print("\n")
    print("Step: ",i+1)
    i+=1
    print("xn = ",round(x,3))
    print('f(xn) = ', round(f(x),3))
    print('f1(xn) = ', round(f1(x),3))
    v = x - (f(x)/f1(x))
    print("xn+1 = ", round(v,3))
    if round(v,3) == round(x,3):
      break
    else:
      x = v
