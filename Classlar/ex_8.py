class Orta_qiymat:
    def __init__(self, age, value):
        self.age = age
        self.value = value

    def myfunction(self):
        print(f"Diaganal yuzi: {int((self.age * self.value) * 0.5)}")


age_value = Orta_qiymat(int(input("x1 : ")), int(input("x2: ")))
age_value.myfunction()
