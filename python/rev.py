n = input("Enter Full Name : ")
s = 0
n.lower()
for a in reversed(n):
    print(a,end="")
for i in reversed(n) :
    if i != " " :
         s+= ord(i)
   
print("\nSUM = ",s)