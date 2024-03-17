import math
class Masofasi :
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def myfunction(self):
        name = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        print(name)
        print("Ular orasidagi masofa:", (self.x1, self.y1, self.x2, self.y2))
total = Masofasi(float(input("A nuqtasi x koordinatini kiriting: ")),
                 float(input("A nuqtasi Y koordinatini kiriting: ")),
                 float(input("B nuqtasi x koordinatini kiriting: ")),
                 float(input("B nuqtasi y koordinatini kiriting: ")))

total.myfunction()