class Ball():
    def __init__(self):
        print(f"It is a ball")
    def Who_I_am(self):
        print(f"I am ball")
class Cricketball(Ball):
    def __init__(self,name):
        self.name = name
    def Who_I_am(self):
        print(f"This is {self.name} ball")
class Foottball(Ball):
    def __init__(self,name):
        self.name = name
    def Who_I_am(self):
        print(f"This is {self.name} ball")
ball = Ball()
ball.Who_I_am()
crikball = Cricketball("Cricket")
football = Foottball("Football")
crikball.Who_I_am()
football.Who_I_am()