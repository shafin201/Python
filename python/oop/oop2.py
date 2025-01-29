#create class 
class Animal():
  #class object attribute
  #same for any instance of class
  species = 'mammal'
  def __init__(self, name, colour):
    #arrtibute
    #we take in the argument
    #assgin it using self.arrtibute_name 
    self.name = name
    self.colour = colour

#create object
tom=Animal('tom', 'gray')
jerry=Animal('jerry', 'browon')

#print object attribute 
print(f'I am tom my species is {tom.species}' )
print(f'I am jerry my species is {jerry.species}')