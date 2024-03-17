class Orta_qiymat:
    def __init__(self, age, value):
        self.age = age
        self.value = value

    def myfunction(self):
        total = (self.age * self.value) ** 0.5
        print(f"O'rta arifmetik {int((self.age + self.value) / 2)}")
        print(f"O'rta geometrik {int(total)}")

age_value = Orta_qiymat(int(input("age: ")), int(input("value: ")))
age_value.myfunction()
