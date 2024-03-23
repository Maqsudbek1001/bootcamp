from abc import ABC, abstractmethod
class KVADRAT(ABC):
    @abstractmethod
    def Kv_ildiz(self):
        pass
class BIKVADRAT(KVADRAT):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Kv_ildiz(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b + D ** 0.5) / (2 * self.a)
            x2 = (-self.b - D ** 0.5) / (2 * self.a)
            return x1, x2
        elif D == 0:
            x = -self.b / (2 * self.a)
            return x
        else:
            return "Bo'sh to'plam"
if __name__ == "__main__":
    a = int(input("son: "))
    b = int(input("son: "))
    c = int(input("son: "))
    kvadrat_tenglama = BIKVADRAT(a, b, c)
    print("Kvadrat tenglama ildizlari:", kvadrat_tenglama.Kv_ildiz())
