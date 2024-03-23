class Yigindi:
    def __init__(self, age):
        self.age = age

    def yigindi(self):
        total = 0
        for i in range(1, self.age):
            total = total + i
        return total


class Kopaytma(Yigindi):
    def __init__(self, age):
        super().__init__(age)

    def kopaytma(self):
        total = 1
        for i in range(1, self.age):
            total *= i
        return total


age = int(input("number: "))
name = Yigindi(age)
name1 = Kopaytma(age)
print(f"Yigindi: {name.yigindi()} Ko'paytma: {name1.kopaytma()}")
