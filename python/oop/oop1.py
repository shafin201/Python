"""class NameOfClass():
  def __init__(self, parameter1, parameter2):
    self.parameter1 = parameter1
    self.parameter2 = parameter2
  
  def someMethod(self):
    #perfrom some action 
    print(self.parameter1)"""

class Animal():
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
print(f'hey! i am {tom.name} and my colour is: {tom.colour}')
print(f'hey! i am {jerry.name} and my colour is: {jerry.colour}')