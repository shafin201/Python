
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
bird = Bird()
spr = sparrow()
ost = ostrich()
 
bird.intro()
bird.flight()
 
spr.intro()
spr.flight()
 
ost.intro()
ost.flight()