import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ekranga_chiqaramiz(self):
        print(f"Vektorlari: ({self.x}, {self.y})")

class Vektor_X_Y(Vektor):
    def qoshish(self, boshqa):
        return Vektor(self.x + boshqa.x, self.y + boshqa.y)

    def ayirish(self, boshqa):
        return Vektor(self.x - boshqa.x, self.y - boshqa.y)

    def skalyar(self, boshqa):
        return self.x * boshqa.x + self.y * boshqa.y

    def uzunligi(self):
        return math.sqrt(self.x**2 + self.y**2)

    def burchak_k(self, boshqa):
        skalyar = self.skalyar(boshqa)
        uzunliklar = self.uzunligi() * boshqa.uzunligi()
        if uzunliklar == 0:
            return None
        return skalyar / uzunliklar

v1 = Vektor_X_Y(3, 4)
v2 = Vektor_X_Y(1, 2)
v1.ekranga_chiqaramiz()
v2.ekranga_chiqaramiz()
qoshilgan = v1.qoshish(v2)
qoshilgan.ekranga_chiqaramiz()
print(f"Skalyar ko'paytma: {v1.skalyar(v2)}")
print(f"V1 uzunligi: {v1.uzunligi()}")
print(f"Burchak kosinusi: {v1.burchak_k(v2)}")
