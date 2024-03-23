class yigindi_kavdrat:
    def __init__(self, age):
        self.age = age

    def main(self):
        name = 0
        total = 0
        for i in range(1, self.age):
            total += (i*i)
            name = total
            print(name)
class Total(yigindi_kavdrat):
    def __init__(self, age):
        super().__init__(age)
age = int(input("son: "))
number = yigindi_kavdrat(age)
print(number.main())


