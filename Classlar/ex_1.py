class person:
    def __init__(self, age, vale):
        self.age = age
        self.value = vale

    def myvakue(self):
        print( self.age+self.value)
age_one = person(int(input("son: ")), int(input("son1 ")))
age_one.myvakue()

