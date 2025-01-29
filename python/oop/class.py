"""def personal_details():
    name, age = "Sakib", '19'
    id = '201-15-3135'
    department = "CSE"
    email = "shakhawat15-3135@diu.edu.bd"
    print("Name: {}\nAge: {}\nId: {}\nDepartment: {}\nEmail: {}".format(name, age, id, department, email))

personal_details()"""

class father:
    def __init__(self, name, gender, char):
        self.name=name
        self.gender=gender
        self.char=char  


    def character(self):
        print(self.name)
        print(self.gender)
        print(self.char)

class child(father):
    def __init__(self, name, gender, char):
        super().__init__(name, gender, char)

    def character(self):
        super().character()

class child1(father):
    def __init__(self, name, gender, char):
        super().__init__(name, gender, char)

    def character(self):
        super().character()


f=father("Khalak"," "," ")
c1=child("Tamim","Male","Good")
c2=child("Akhi","Female","Bad")

print("Father")
f.character()
print("\nChildern 1")
c1.character()
print("\nChildern 2")
c2.character()