class Father:
    def __init__(self,name):
        self.name = name
       
    def info(self):
        print(f"{self.name}")
        print(f"Two child")
       
class Boy(Father):
    def __init__(self,name,gender):
        super().__init__(name)
        self.gender = gender
    def info(self):
        print(f"I am {self.name}")
        print(f"Gender {self.gender}")
        print(f"He has good character")
class Girl(Father):
    def __init__(self,name,gender):
        super().__init__(name)
        self.gender = gender
    def info(self):
        print(f"I am {self.name}")
        print(f"Gender {self.gender}")
        print(f"She has bad character" )
       
f = Father("AAAAAA")
f.info()
b = Boy("Shafin","Male")
b.info()
g = Girl("Tomuk","Female")
g.info()