import math
class yuzasi:
    def __init__(self, age):
        self.age = age


    def myfunction(self):
        print(f"doira radiusi {(self.age/3.14)**0.5}")



age_value = yuzasi(int(input("age: ")))
age_value.myfunction()
