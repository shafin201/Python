class Shop:
    def __init__(self, name, location):
        self.name = name
        self.location = location
 
    def sell(self):
        pass
 
class Dressshop(Shop):
     def __init__(self, name, location):
        super().__init__(name, location)
 
        print(f'This shop name is {self.name}')
        print(f'This shop location is {self.location}')
 
     def sell(self):
        print("Dress Are Sell")
  
 
class Foodshop(Shop):
    def __init__(self, name, location):
        super().__init__(name, location)
 
        print(f'This shop name is {self.name}')
        print(f'This shop location is {self.location}')
 
    def sell(self):
        print("Food Are Sell")
print('Shop 1:') 
shop1 = Dressshop('Anzara','Dhaka')
shop1.sell()
print('Shop 2:')
shop2 = Foodshop('Chillox', 'Uttara')
shop2.sell()



#1st stor
[1,2]
[3,4]
#2nd stor
[5,6]
[7,8]