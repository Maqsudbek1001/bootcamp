class Uchburchak:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
    def hisobla(self):
        heron = (self.x+self.y+self.c)/2
        return (heron*(heron-self.x)*(heron-self.y)*(heron-self.c))**0.5
class Program(Uchburchak):
    def __init__(self, x, y, c):
        super().__init__(x, y, c)
age1 = int(input("son: "))
age2 = int(input("son: "))
age3 = int(input("son: "))
total = Uchburchak(age1, age2, age3)
print(total.hisobla())
