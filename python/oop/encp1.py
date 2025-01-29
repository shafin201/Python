class Edu():
    def __init__(self):
        self.course ="Programing cource"
        self.tech="Python"
    def Name(self):
        return self.course + self.tech

e = Edu()
print(e.course)
print(e.tech)
print(e.Name())