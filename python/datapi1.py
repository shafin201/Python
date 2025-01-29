#Program No:1
x = 'hellow'
print(x[1])

#Program No:2
x = 'hellow'
print(x[-1])

#Program No:3
x = 'hellow'
for c in x:
    print(c)

#Project:1
count = 0
str = input('Enter string :')
for i in str:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
       count+=1
print(count)

#Program No:4
x = " I had a book"
if "book" in x:
    print("Yes")

#Program No:5
x = "This is a book"

print(x.count("i"))
print(x.upper())
print(x.lower())
print(x.replace("a book"," a pen"))
print(len(x))

#Program No:6
a = input()
b = input()
c = len(a)
print(int((a.count(b)/c)*100))

#Program No:7
x = [1 , 2 , 3 ,4]
res = 1
for n in x:
    res*=n
print(res)

#Program No:8
x = [1 , 2 , 3 ,4]
x.append(8)
x.remove(4)
x.insert(0,6)
print(x)
print(x.count(8))

#Program No:9
x = [1 , 5 , 3 ,2]
x.reverse()
print(x)
x.sort()
print(x)
"""print(min(x))
print(max(x))

#Program No:10
nums = [i*2 for i in range(10)]
print(nums)

#Program No:11
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])"""

def f(x):
    p = (x**2)-2*x-3
    return p


x = float(input())
x1 = float(input())

print("Newton rapson Solution: ")
i = 0
while True:
    print("\n")
    print("Step: ",i+1)
    i+=1
    print(" = ",round(x,3))
    v = (x + x1)/2
    print("fx = ", round(v,3))
    if round(v,3) == round(x,3):
      break
    else:
      x = v







