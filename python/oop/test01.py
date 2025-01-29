class Shop():
    def __init__(self,name,location):
        self.name = name
        self.location = location
        
    def sell(self):
        print(self.name)
        print(self.location)
class Dress_shop(Shop):
    def __init__(self, name, location):
        super().__init__(name, location)
    def sell(self):
        super().sell()
class Food_shop(Shop):
    def __init__(self, name, location):
        super().__init__(name, location)
    def sell(self):
        super().sell()

s = Shop("Two Shop"," ")
d = Dress_shop("Dress shop","Dhaka")
f = Food_shop("Food shop","Narayangonj")

s.sell()
print("Shop 1 :")
d.sell()
print("Shop 2 :")
f.sell()
