r = int(input("Row : "))
c = int(input("coloum : "))
mat=[]
print("Enter Name Roll and Age : ")
for i in range(r):
  mat.append([])
 # print("Enter Name Roll and Age : ")
  print("Student :",i+1)
  for j in range(c):
    x = input()
    mat[i].append(x)
print(mat)