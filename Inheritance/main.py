import math

class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def kop_aytma(self):
        return self.x * self.y

    def bo_linma(self):
        return self.x / self.y

    def yi_gindi(self):
        return self.x + self.y

    def ayir_ma(self):
        return self.x - self.y

    def max(self):
        return max(self.x, self.y)

    def min(self):
        return min(self.x, self.y)

    def orta_arifmetik(self):
        return (self.x + self.y) / 2

    def orta_geom(self):
        return math.sqrt(self.x * self.y)

class Total(Person):
    def __init__(self, x, y):
        super().__init__(x, y)

age1 = int(input("1 son: "))
age2 = int(input("2 son: "))
total = Total(age1, age2)
print(total.min())
