class Max_Min(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def ikta_son(self):
        eng_kata = max(self.x, self.y)
        eng_kichig = min(self.x, self.y)
        print(f"enga kattasi {eng_kata} va kichigi {eng_kichig}")
    def uchtason(self):
        eng_kata = max(max(self.x, self.y), self.z)
        eng_kichig = min(min(self.x, self.y), self.z)
        print(f"Eng kattasi {eng_kata} va kichigi {eng_kichig}")

class Total(Max_Min):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
age = int(input("son "))
age1 = int(input("son "))
age2 = int(input("son "))
umumiy = Max_Min(age, age1, age2)

print(umumiy.uchtason())