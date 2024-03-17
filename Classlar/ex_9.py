class Orta_qiymat:
    def __init__(self, x1):
        self.x1 = x1


    def myfunction(self):
        a = int(self.x1 % 10)
        b = int((self.x1/100)%10)
        c = int((self.x1/10)%10)
        print(f"Raqamlari yigindisi: {a+b+c}")
        print(f"Raqamlari ko'paytmasi {a*b*c} ")




age_value = Orta_qiymat(int(input("x1 : ")))
age_value.myfunction()
