class HaftaKuni:
    def __init__(self, n):
        self.n = n

    def switch_n(self):
        switcher = {1: "Dushanba", 2: "Seshanba", 3: "Chorshanba", 4: "Payshanba", 5: "Juma", 6: "Shanba",
            7: "Yakshanba"}
        return switcher.get(self.n, "Noto'g'ri kuni raqami")


class OyNomi:
    def __init__(self, m):
        self.m = m

    def switch_m(self):
        switcher = {1: "Yanvar", 2: "Fevral", 3: "Mart", 4: "Aprel", 5: "May", 6: "Iyun", 7: "Iyul", 8: "Avgust",
            9: "Sentabr", 10: "Oktabr", 11: "Noyabr", 12: "Dekabr"}
        return switcher.get(self.m, "Noto'g'ri oy raqami")


class HaftaKuniOyNom(HaftaKuni, OyNomi):
    def __init__(self, n, m, k):
        HaftaKuni.__init__(self, n)
        OyNomi.__init__(self, m)
        self.k = k
        self.m = m
        self.k = k

    def total(self):
        hafta_kuni = self.switch_n()
        oy_nom = self.switch_m()
        print(f"Kiritilgan son {self.k} ni ifodalaydigan so'z: {hafta_kuni} va {oy_nom}")


# Asosiy dastur
n = int(input("1 dan 7 gacha raqam: "))
m = int(input("1 dan 12 gacha bir oy raqamini: "))
k = int(input("1 dan 12 gacha raqam: "))

obj = HaftaKuniOyNom(n, m, k)
obj.total()

