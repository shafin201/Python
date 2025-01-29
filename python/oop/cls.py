"""class Animal():
  def __init__(self, name, colour):
    #arrtibute
    #we take in the argument
    #assgin it using self.arrtibute_name 
    self.name = name
    self.colour = colour
  def running(self):
    print(f'hey! i am {self.name}, now i am running!')
  def drinkingMilk(self):
    print(f'hey! i am {self.name}, now i am drinking mlik!')

tom=Animal('tom', 'gray')
jerry=Animal('jerry', 'browon')

tom.running()
tom.drinkingMilk()
print("\n")
jerry.running()
jerry.drinkingMilk()"""

"""class Animal():
  def __init__(self, objectName, objectColour):
    #arrtibute
    #we take in the argument
    #assgin it using self.arrtibute_name 
    self.name = objectName
    self.colour = objectColour

#create object
tom=Animal('tom', 'gray')
jerry=Animal('jerry', 'browon')

#printing object attribute, object attribute access with name and colour. 
print(f'hey! i am {tom.name} and my colour is: {tom.colour}')
print(f'hey! i am {jerry.name} and my colour is: {jerry.colour}')"""

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeksll"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
        print(self.a)
# Driver code
obj1 = Base()
print(obj1.a)
print(obj1._Base__c)
