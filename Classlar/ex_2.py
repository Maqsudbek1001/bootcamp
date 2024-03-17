class kub:
    def __init__(self, age, value):
        self.age = age
        self.value = value

    def myfunction(self):
        print(f"yuzi {self.age * self.value}")
        print(f"perimetri {2 * (self.age + self.value)}")


age_value = kub(int(input("age: ")), int(input("value: ")))
age_value.myfunction()
