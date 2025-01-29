class Shop():
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def sell(self):
       pass
class Dress_shop(Shop):
    def __init__(self, name, location):
        super().__init__(name, location)

        print(f'The shop name is {self.name}')
        print(f'The location name is {self.location}')

    def sell(self):
        print('Dresss are sell')
class Food_shop(Shop):
    def __init__(self, name, location):
        super().__init__(name, location)
        print(f'The shop name is {self.name}')
        print(f'The location name is {self.location}')
    def sell(self):
         print('Foods are sell')

print("Shop 1 :")
d = Dress_shop("Dress shop","Dhaka")
d.sell()
print("Shop 2 :")
f = Food_shop("Food shop","Narayangonj")
f.sell()



