class radius:
    def __init__(self, age):
        self.age = age


    def myfunction(self):
        print(f"aylana uzinligi {self.age * 2* 3,14}")
        print(f"doira yuzi {3,14*self.age**2}")


age_value = radius(int(input("age: ")))
age_value.myfunction()
