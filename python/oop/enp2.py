
# Python program to
# demonstrate protected members
  
class Base:
    def __init__(self):
         
        self._a = "201-15-3233"
        self.__b = "Shafin Tamim"
 
# Creating a derived class   
class Derived(Base):
    def __init__(self):
         
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)
        print(self.__b)
 

         
obj2 = Base()
print(obj2._a)
print(obj2._Base__b)
 
# Calling protected member
# Outside class will  result in
# AttributeError
#print(obj2.a)