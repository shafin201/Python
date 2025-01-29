"""i = 3
while i >=  0:
    print(i)
    i = i-1
print("Finished!") """

"""x = 1
while x < 10:
    if x%2 == 0 :
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    #x += 1 """

"""x = 0
while x <= 20:
     print(x)
     x+= 2"""

"""i = 0
x = 0
while i < 4:
    x+=i
    i+=1
print(x)"""

"""x = float(input())
b = (x**3)-3*x-3
print(round(b,3))"""


"""def f(x):
    p =(2*(x**2)-(2*x)-5)
    return p

def f1(x):
    p = (4*x-2)
    return p

x = float(input())
print("Newton rapson Solution: ")
for i in range(5):
    print("\n")
    print("Step: ",i+1)
    print("xn = ",round(x,3))
    print('f(xn) = ', round(f(x),3))
    print('f1(xn) = ', round(f1(x),3))
    v = x - (f(x)/f1(x))
    print("xn+1 = ", round(v,3))
    x = v"""

import math
def f(c):
    p = math.cos(c) + 5 * c - 8
    return p

def f1(c):
    p = -math.sin(c) + 5
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